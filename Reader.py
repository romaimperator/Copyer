from multiprocessing import Process

class Reader(Process):
    def __init__(self, pipe):
        super(Reader, self).__init__()
        self.pipe = pipe


    def run(self):
        pass


    def read_data(self, data):
        pass
