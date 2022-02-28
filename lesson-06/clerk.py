import queue
from socket import AI_PASSIVE


class Queue:
    queue = []
    def push(self,item):
        self.queue.append(item)
        self.
        pass
    def get(self):
        return self.queue.pop(0)
        pass

import multiprocessing,os

def say(what):
    print('Process %s says:')