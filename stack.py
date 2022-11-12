from collections import deque

#Implementation using deque class.
class Stack():
    def __init__(self):
        self.arr = deque()

    def __str__(self):
        values = [str(x) for x in self.arr]
        for v in values:
            print(v)
        return
    def push(self, data):
        self.arr.append(data)

    def pull(self):
        return self.arr.pop()

    def peek(self):
        self.arr[-1]

    def length(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def reverse_string(self, string):
        reversed_str = ""
        for char in string:
            self.push(char)
        while self.arr:
            reversed_str += self.pull()
        print(reversed_str)
        return reversed_str

#Implementing using linked list.
class LLStack():
    def __init__(self):
        self.head = None

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
    
class Stack2():
    def __init__(self):
        self.arr = LLStack()

    def isEmpty(self):
        if self.arr.head == None:
            return True
        return False
    
    def __str__(self):
        llstr = ""
        itr = self.arr.head
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        return llstr

    def __len__(self):
        count = 0
        itr = self.arr.head
        while itr:
            count += 1
            itr = itr.next
        return count 
    
    def push(self, data):
        node = Node(data)
        node.next = self.arr.head
        self.arr.head = node
        return

    def pop(self):
        if self.isEmpty():
            return "There is nothing to return"
        val = self.arr.head.data
        itr = self.arr.head
        self.arr.head = itr.next
        return val

    def peek(self):
        if self.isEmpty():
            return "There is nothing to return"
        return self.arr.head.data 
    
    def delete(self):
        self.arr.head = None

#Q1 Valid parenthesis if every left parenthesis "(" is closed by a right one ")"
def valid_parenthesis(string: str):
    stq = Stack2()
    for i in range(len(string)):
        if string[i] == "(":
            stq.push(i)
        else:
            if stq.isEmpty():
                return False
            stq.pop()
    if stq.isEmpty():
        return True
    return False       

#Q2
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

#Q3 Stack Min. A method that can find the minimum stack element in 0(1) time. Decided to use a 'mini-stack' 
class llStack():                                            #for the minimums within the main stack class.
    def __init__(self):
        self.head = None

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

class MinStack():
    def __init__(self):
        self.arr = llStack()
        self.mini = None

    def min(self):
        if not self.mini:
            return None
        return self.mini.data
    
    def push(self, data):
        if not self.arr.head:
            node = Node(data)
            self.arr.head = node
            self.mini = node
        else:
            node = Node(data)
            node.next = self.arr.head
            self.arr.head = node
            if self.arr.head.data < self.mini.data:
                node.next = self.mini
                self.mini = node
            return
    
    def pop(self):
        if self.arr.head == None:
            return "There is nothing to return"
        val = self.arr.head.data
        itr = self.arr.head
        self.arr.head = itr.next
        if val == self.mini.data:
            self.mini = self.mini.next
            # return self.mini
        return val

#Q4 Stack of plates. When it reaches a certain capacity, we need to begin a new stack.

class Stack3():
    def __init__(self, stack_size) -> None:
        self.stack_size = stack_size
        self.stacks = []
    
    def __str__(self):
        # print(self.stacks)
        return str(self.stacks)

    def push(self, data):
        if len(self.stacks) and len(self.stacks[-1]) < self.stack_size:
            self.stacks[-1].append(data)
        else:
            self.stacks.append([data])
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return "The whole stack is empty"
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stack_num):
        if stack_num >= len(self.stacks):
            raise Exception("Invalid index")
        elif len(self.stacks[stack_num]) > 0:
            return self.stacks[stack_num].pop()
        return None

#Q5 Implemnt a queue via two stacks.

class Stack5():
    def __init__(self) -> None:
        self.arr = []
    
    def __len__(self):
        return len(self.arr)

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        if len(self.arr) == 0:
            return None
        return self.arr.pop()

class QueueViaStack():
    def __init__(self) -> None:
        self.in_stack = Stack5()
        self.out_stack = Stack5()
    
    def enqueue(self, data):
        self.in_stack.push(item=data)
    

    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return result

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


class Queue6():
    def __init__(self) -> None:
        self.arr = llStack6()
    
    def enqueue(self, data):
        if not self.arr.head:
            node = Node(data)
            self.arr.head = node
            self.arr.head = node
            self.arr.tail = node
        else:
            node = Node(data)
            node.next = self.arr.head
            self.arr.head = node
    
    def dequeue_any(self):
        data = self.arr.tail.data
        self.arr.tail = self.arr.tail.prev


st = QueueViaStack()
st.enqueue(5)
st.enqueue(1)
st.enqueue(9)
st.enqueue(55)
st.enqueue(98)
print(st.dequeue())
print(st.dequeue())
print(st.dequeue())
print(st.dequeue())