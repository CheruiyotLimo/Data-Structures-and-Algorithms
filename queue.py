from collections import deque
class Queue():
    def __init__(self) -> None:
        self.arr = deque()
    def enqueue(self, data):
        self.arr.appendleft(data)

    def dequeue(self):
        return self.arr.pop()

    def peek(self):
        self.arr[-1]

    def length(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0
