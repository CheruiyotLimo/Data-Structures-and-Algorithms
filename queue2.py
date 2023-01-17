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

#Q1
#Three in one. Convert a python list into three stacks
class MultiStack():
    def __init__(self, stacksize) -> None:
        self.number_stacks = 3
        self.cust_list = [0] * (self.number_stacks * stacksize)
        self.sizes = [0] * self.number_stacks
        self.stacksize = stacksize

    def is_full(self, stack_num):
        if self.sizes[stack_num] == self.stacksize:
            return True
        return False
    
    def is_empty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        return False
    
    def is_top_element(self, stack_num):
        offset = stack_num * self.stacksize
        return offset + self.sizes[stack_num]-1

    def push(self, data, stack_num):
        if self.is_full(stack_num):
            return "The stack is full"
        else:
            self.sizes[stack_num] += 1
            self.cust_list[self.is_top_element(stack_num)] = data

    def pop(self, stack_num):
        if self.is_full(stack_num):
            return "The stack is full"
        else:
            value = self.cust_list[self.is_top_element(stack_num)]
            self.cust_list[self.is_top_element(stack_num)] = 0
            self.sizes[stack_num] -= 1
            return value

    def peek(self, stack_num):
        if self.is_full(stack_num):
            return "The stack is full"
        else:
            value = self.cust_list[self.is_top_element(stack_num)]
            return value

#Q6 Animal shelter.
class llStack6():                                            
    def __init__(self):
        self.head = None
        self.tail = None

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

class Queue6():
    def __init__(self) -> None:
        self.arr = llStack6()
    
    def __str__(self):
        llstr = ""
        itr = self.arr.head
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
            if itr.next == self.arr.head.next:
                break
        return llstr

    def enqueue(self, data):
        if not self.arr.head:
            node = Node(data)
            node.prev = node
            node.next = node
            self.arr.head = node
            self.arr.head = node
            self.arr.tail = node
        else:
            node = Node(data)
            node.next = self.arr.head
            node.prev = self.arr.tail
            self.arr.head.prev = node
            self.arr.head = node
            self.arr.tail.next = node
    
    def dequeue_any(self):
        data = self.arr.tail.data
        self.arr.tail = self.arr.tail.prev
        self.arr.head.prev = self.arr.tail
        self.arr.tail.next = self.arr.head
        return data
    
    def dequeue_dog(self):
        if self.arr.tail.data == "Dog":
            return self.dequeue_any()
        else:
            itr = self.arr.tail.prev
            while itr:
                if itr.data == "Dog":
                    x = itr.data
                    if itr == self.arr.head:
                        self.arr.head = itr.next
                        self.arr.head.prev = self.arr.tail
                        self.arr.tail.next = self.arr.head
                    else:
                        itr.prev.next = itr.next
                        itr.next.prev = itr.prev
                    return x
                itr = itr.prev
                if itr.prev == self.arr.tail.prev:
                    break       

    def dequeue_cat(self):
        if self.arr.tail.data == "Cat":
            return self.dequeue_any()
        else:
            itr = self.arr.tail.prev
            while itr:
                if itr.data == "Cat":
                    x = itr.data
                    if itr == self.arr.head:
                        self.arr.head = itr.next
                        self.arr.head.prev = self.arr.tail
                        self.arr.tail.next = self.arr.head
                    else:
                        itr.prev.next = itr.next
                        itr.next.prev = itr.prev
                    return x
                itr = itr.prev
                if itr.prev == self.arr.tail.prev:
                    break                

qu = Queue6()
qu.enqueue("Cat")
qu.enqueue("Cat")
qu.enqueue("Dog")
qu.enqueue("Dog")
qu.enqueue("Cat")
print(qu.dequeue_cat())
print(qu.dequeue_cat())
print(qu.dequeue_cat())
print(qu)