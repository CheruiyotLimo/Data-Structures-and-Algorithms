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

st = Stack2()
print(st.isEmpty())
st.push(1)
st.push(2)
st.push(3)
st.push(5)
print(st)
# print(len(st))
print(st.pop())
print(st.peek())
print(st)