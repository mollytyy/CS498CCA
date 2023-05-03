import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        # self._context = context

        storm.logInfo("Counter bolt instance starting...")
        # Task: set N
        self._n = int(self._conf['N'])
        self.heap = []
        heapq.heapify(self.heap)
        self._counter = Counter()
        # End

        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        '''
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        result: "far 11, oh 12, yet 16, up 14, get 14, ye 19, no 20, sir 21, mr 16, day 16" (the order does not matter here)
        '''
        word = tup.values[0]
        self._counter[word] += 1
        count = self._counter[word]
        # storm.logInfo(str((count, word)))

        if len(self.heap) == self._n and count > min(self.heap, default=(float('-inf'), None))[0]:
            cur = self.heap
            self.heap = [(c, w) for c, w in self.heap if w != word]
            if len(cur) != len(self.heap):
                heapq.heappush(self.heap, (count, word))
            else:
                heapq.heappushpop(self.heap, (count, word))
            storm.emit([[x[1] for x in self.heap]])

        if len(self.heap) < self._n:
            self.heap = [(c, w) for c, w in self.heap if w != word]
            heapq.heappush(self.heap, (count, word))

        # if (len(self.heap) <= self._n) and count > min(self.heap, default=(float('-inf'), None))[0] and count > 10:
        #     if word in [x[1] for x in self.heap]:
        #         # update heap
        #         # storm.logInfo("2")
        #         # storm.logInfo("before: %s" % str(self.heap))
        #         self.heap = [(c, w) for c, w in self.heap if w != word]
        # #         self.heap = heapq.heapify(heap_items)
        #         heapq.heappush(self.heap, (count, word))
        #         # storm.logInfo("after: %s" % str(self.heap))

        #     else:
        #         # storm.logInfo("1")
        #         heapq.heappush(self.heap, (count, word))

        #     storm.emit([[x for x in self.heap]])

        # End


# Start the bolt when it's invoked
TopNFinderBolt().run()
