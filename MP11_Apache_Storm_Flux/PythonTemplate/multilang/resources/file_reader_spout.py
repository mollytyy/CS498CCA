# from os.path import join
from time import sleep

# from streamparse import Spout
import storm


class FileReaderSpout(storm.Spout):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._complete = False

        # storm.logInfo("filepath: %s" % self._conf['filepath'])
        storm.logInfo("Spout instance starting...")

        # Task: Initialize the file reader
        # hint: get the filename from conf argument
        self._file = open(self._conf['filepath'])
        # End

    def nextTuple(self):
        # Task 1: read the next line and emit a tuple for it
        # Task 2: don't forget to sleep for 1 second when the file is entirely read to prevent a busy-loop

        if not self._complete:
            try:
                next_line = next(self._file)
                if next_line == '\n':
                    next_line = next(self._file)
                next_line = next_line.replace('.', '')
                # storm.logInfo(f"SpoutEmitting: {next_line}")
                storm.emit([next_line])
            except StopIteration:
                self._complete = True
                self._file.close()
                sleep(1)
            # sleep(1)
        # End


# Start the spout when it's invoked
FileReaderSpout().run()
