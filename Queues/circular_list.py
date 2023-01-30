#Implementation using a circular queue.
#A bit more complex implementation but better performance time compared to normal python list implementation.

class Queue3():
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.items = max_size * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        values = " ".join(values)
        return values

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        return False
    
    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception ("The queue is already full.")
        else:
            if self.top + 1 == self.max_size:
                self.start = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = data
    
    def dequeue(self):
        if self.is_empty():
            raise Exception ("The queue is empty.")
        else:
            first_element = self.items[self.start]
            start_ind = self.start
            if self.start == self.top:   #Checking to see if it is the only element in the queue.
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start_ind] = None
            return first_element

    def peek(self):
        if self.is_empty():
            raise Exception ("The queue is empty.")
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max_size * [None]
        self.start = -1
        self.top = -1