from collections import deque
class Stack():
    def __init__(self):
        self.arr = deque()

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
st = Stack()
st.arr
st.reverse_string("We will conquere COVID-19") 