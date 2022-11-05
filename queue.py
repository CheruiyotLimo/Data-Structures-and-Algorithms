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

qu = Queue2()
print(qu.isEmpty())
qu.enqueue(2)
qu.enqueue(54)
qu.enqueue(3)
qu.enqueue(5)
qu.enqueue(7)
print(qu.dequeue())
print(qu.peek())
# print(len(qu))
print(qu)