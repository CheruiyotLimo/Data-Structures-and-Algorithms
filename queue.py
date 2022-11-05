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

class LLStack():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr
            itr = itr.next

    def __str__(self):
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        return llstr
    
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue2():
    def __init__(self):
        self.arr = LLStack()
    
    def __str__(self):
        llstr = ""
        itr = self.arr.head
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
            if itr.next == self.arr.head.next:
                break
        return llstr

    def __len__(self):
        count = 0
        itr = self.arr.head
        while itr:
            count += 1
            itr = itr.next
            if itr.next == self.arr.head.next:
                break
        return count 

    def isEmpty(self):
        if self.arr.head == None:
            return True
        return False
    
    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty():
            node.next = node
            node.prev = node
            self.arr.head = node
            self.arr.tail = node
        else:
            node.next = self.arr.head
            node.prev = self.arr.tail
            self.arr.head.prev = node
            self.arr.head = node
            self.arr.tail.next = node
        return

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        x = self.arr.head.prev.data
        self.arr.tail = self.arr.tail.prev
        self.arr.tail.next = self.arr.head
        self.arr.head.prev = self.arr.tail
        return x

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.arr.head.prev.data

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


qu = Queue3(3)
print(qu.is_full())
print(qu.is_empty())
qu.enqueue(5)
qu.enqueue(7)
# qu.enqueue(8)
qu.enqueue(9)
print(qu.dequeue())
print(qu.peek())
# print(qu.dequeue())
# print(qu.dequeue())
# print(qu.dequeue())
qu.delete()
print(qu)
print(qu.is_full())
print(qu.is_empty())