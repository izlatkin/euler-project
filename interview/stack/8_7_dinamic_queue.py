import collections


class QueueWithMax:
    def __int__(self):
        self._entries = collections.deque()
        self._candidates_for_max = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)

    def dequeue(self):
        result = self._entries.popleft()
        if result == self._candidates_for_max[0]:
            self._candidates_for_max.popleft()
        return result

    def max(self):
        return self._candidates_for_max[0]

class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self._entries = [0] * capacity
        self._head = self._tail = self._number_queue_elements = 0

    def enqueue(self, x: int) -> None:
        if self._number_queue_elements == len(self._entries): # need resize
            self._entries = (self._entries[self._head:] + self._entries[:self._head])
            self._head, self._tail = 0, self._number_queue_elements
            self._entries += [0] * (len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._number_queue_elements += 1

    def dequeue(self) -> int:
        self._number_queue_elements -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result

    def size(self) -> int:
        return self._number_queue_elements

    def print(self) -> None:
        #end = max(self._tail, len(self._entries))
        for i in range(self._head, self._head + self._number_queue_elements):
            print(self._entries[i], end=' ')
        print()



def main():
    queue = Queue(10)
    for i in range(10):
        queue.enqueue(i)
    queue.print()

    for i in range(5):
        queue.dequeue()
    queue.print()

    for i in range(5):
        queue.dequeue()
    queue.print()

    n  = 100
    for i in range(n):
        queue.enqueue(i)
    queue.print()

    for i in range(n // 2):
        queue.dequeue()
    queue.print()

    for i in range(n // 2):
        queue.dequeue()
    queue.print()

if __name__ == '__main__':
    main()