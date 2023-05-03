import storm
import redis


class TopNStoreBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        # redis configuration converted into a dictonary
        self._redis = conf.get("redis")
        storm.logInfo("Top N Store bolt instance starting...")
        self.r = redis.Redis(host=self._redis['host'], port=self._redis['port'],
                             password=self._redis['password'], db=self._redis['db'], socket_timeout=self._redis['timeout'])
        # Connect to Redis using redis.Redis() with redis configuration in self._redis dictionary
        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        # Task: save the top-N word to redis under the specified hash name
        ret = ''
        first = True
        for word in tup.values[0]:
            if first:
                first = False
                ret += str(word)
            else:
                ret += ', ' + str(word)

        self.r.hset(self._redis['hashKey'], "top-N", ret)
        # End


# Start the bolt when it's invoked
TopNStoreBolt().run()
