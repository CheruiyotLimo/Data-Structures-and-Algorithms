

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