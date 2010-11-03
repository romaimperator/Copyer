from multiprocessing import Process, Queue
from __future__ import with_statement

class FileCopy(Process):
    def __init__(self, filename, dest):
        super(FileCopy, self).__init__()
        self.filename = filename
        self.BUFFER_SIZE = 1024 * 1024


    def run(self):
        self.queue = Queue()
        self.writer = Writer(self.queue, dest)
        self.writer.start()

        with open(self.filename, 'rb') as f:
            data = f.read(self.BUFFER_SIZE)
            self.queue.put(["data", data])

