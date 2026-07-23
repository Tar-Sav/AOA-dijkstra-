import itertools
from heapq import heappush, heappop


class PriorityQueue:

    def __init__(self):

        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = itertools.count()


    def __len__(self):

        return len(self.pq)


    def add_task(self, priority, task):

        if task in self.entry_finder:

            self.remove_task(task)


        count = next(self.counter)

        entry = [priority, count, task]

        self.entry_finder[task] = entry

        heappush(self.pq, entry)



    def remove_task(self, task):

        entry = self.entry_finder.pop(task)

        entry[-1] = self.REMOVED



    def pop_task(self):

        while self.pq:

            priority, count, task = heappop(self.pq)

            if task != self.REMOVED:

                del self.entry_finder[task]

                return priority, task


        raise KeyError("Priority queue is empty")