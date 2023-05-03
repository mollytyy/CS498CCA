import storm
import redis


class WordCountStoreBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        # redis configuration converted into a dictonary
        self._redis = conf.get("redis")
        storm.logInfo("Word Count Store bolt instance starting...")

        # Connect to Redis using redis.Redis() with redis configuration in self._redis dictionary
        # Hint: Add necessary instance variables and classes if needed
        self.r = redis.Redis(host=self._redis['host'], port=self._redis['port'],
                             password=self._redis['password'], db=self._redis['db'], socket_timeout=self._redis['timeout'])

    def process(self, tup):
        # Task: save word count pair to redis under the specified hash name
        word = tup.values[0]
        count = tup.values[1]
        # storm.logInfo(f"word: {word}, count: {count}")
        self.r.hset(self._redis['hashKey'], word, count)
        # End


# Start the bolt when it's invoked
WordCountStoreBolt().run()
