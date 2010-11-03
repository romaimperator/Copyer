from multiprocessing import Process

class Writer(Process):
    """
    Separate process to write the file to disk.
    """

    def __init__(self, queue, filename):
        super(Writer, self).__init__()
        self.BUFFER_SIZE = 1024 * 1024
        self.queue = queue
        self.filename = filename


    def run(self):
        self.outfile = open(self.filename, 'wb')

        while(1):
            data = self.queue.recv()
            if data[0] == "done":
                break
            write_data(data[1])

        self.outfile.close()
                        

    def write_data(self, data):
        self.outfile.write(data)
