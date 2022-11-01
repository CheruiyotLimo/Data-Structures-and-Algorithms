
from random import randint
from tkinter import N


class Node():
    def __init__(self, prev, data, next):
        self.data = data
        self.prev = prev
        self.next = next
    
class CDLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.head is None:
            print("The linked list is empty")
            return
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + "-->"
            if itr.next == self.head:
                break
            itr = itr.next
        # print(llstr)
        return llstr

    def add_to_beginning(self, data):
        if not self.head:
            node = Node(prev=None, data=data, next=None)
            node.next = node
            node.prev = node
            self.head = node
            self.tail = node
            self.tail.next = node
            # print("here")
        else:
            node = Node(prev=self.tail, data=data, next=self.head)
            self.head.prev = node
            self.head = node
            self.tail.next = node
            # print("there")
            return
    
    def add_to_end(self, data):
        itr = self.head
        while itr:
            if itr.next == self.head:
                node = Node(prev=self.tail, data=data, next=self.head)
                self.tail.next = node
                self.tail = node
                self.head.prev = self.tail
                break
            itr = itr.next
        return
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            if itr.next == self.head:
                break
            itr = itr.next
        return count    

    def insert_at(self, data, location):
        if location < 0 or location > self.get_length():
            raise Exception("Index Error: The index is unavailable.")
        if location == 0:
            return self.add_to_beginning(data=data)
        if location == self.get_length():
            return self.add_to_end(data=data)
        itr = self.head
        index = 0
        while itr:
            if index == location-1:
                node = Node(prev=itr, data=data, next=itr.next)
                itr.next = node
                node.next.prev = node
                break
            itr = itr.next
            index += 1

    def remove_at(self, location):
        if location < 0 or location >= self.get_length():
            raise Exception("Index Error: The index is unavailable.")
        if location == 0:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            return
        elif location == self.get_length():
            self.tail = self.tail.prev
            self.head.prev = self.tail
            self.tail.next = self.head
            return
        count = 0
        itr = self.head
        while itr:
            if count == location-1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            count += 1
            itr = itr.next

    def generate(self, n, min, max):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add_to_beginning(randint(min, max))
        return 
    #Solving several challenging interview questions

    #Q1 Removing any duplicates from a linked list
    #Method 1
    def remove_duplicates(self):
        itr = self.head
        checklist = [itr.data]
        count = 0
        while itr:
            if self.head == None:
                return "The linked list is empty."
            else:
                if itr.next.data in checklist:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                else:
                    checklist.append(itr.next.data)
                    itr = itr.next
            if itr.next == self.head:
                break
    #Method2 Solves without using a temporary storage i.e. the checklist above.
    #time complexity n^2 but space coplexity is 0(1)
    def remove_duplicates_2(self):
        if self.head == None:
            return
        itr = self.head
        while itr:
            ath = itr
            while ath:
                if itr.data == ath.next.data:
                    ath.next = ath.next.next
                    ath.next.prev = ath
                else:
                    ath = ath.next
                if ath.next == self.head:
                    break
            itr = itr.next
            if itr.next == self.head:
                    break

    #Q2 
    #Return Nth element from the last.
    #method 1
    def return_from_last(self, n):
        if self.head == None:
            return
        itr = self.tail
        count = 0
        while itr:
            if count == n-1:
                return itr.data
            count += 1
            itr = itr.prev
            if itr.prev == self.tail:
                break
    
    #Method 2
    def two_pointer(self, n):
        if self.head == None:
            return
        itr1 = self.head
        itr2 = self.head
        while n:
            n -=1
            itr1 = itr1.next
            
        while itr1 is not self.tail:
            itr1 = itr1.next
            itr2 = itr2.next
        return itr2.next.data

    #Q3 Partition a linked list around  value.
    #Method1
    def partitioner(self, val):
        itr = self.head
        self.tail = self.head
        while itr:
            next_node = itr.next
            itr.next = None
            if itr.data < val:
                itr.next = self.head
                self.head = itr
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                self.tail.next = itr
                self.tail = itr
                self.tail.next = self.head
            itr = itr.next
            # if itr.next == self.tail:
            #     break
        # return
        if self.tail.next is not None:
            self.tail.next = None
    
    #Q4 Sum of two numbers represented as linked lists returning it as another linked list.
def sum_of_ll(list1, list2):
    itr = list1.head
    itr2 = list2.head
    carry = 0
    new_ll = CDLinkedList()
    while itr or itr2:
        result = carry
        if itr:
            result += itr.data
            itr = itr.next
        if itr2:
            if itr2 == list2.tail:
                result += itr2.data
                new_ll.add_to_beginning(int(result))        #It should print the new linked in reverse order
                return new_ll                               #so I should use the add_to_end method but it seems
            result += itr2.data                             #bugged at the moment. Will investigate.
            itr2 = itr2.next
        new_ll.add_to_beginning(int(result % 10))
        carry = result / 10
        if itr2.next == list2.head.next:
            break
    return new_ll

ll = CDLinkedList()
# ll.create(12)
ll.add_to_beginning(5)
ll.add_to_beginning(8)
ll.insert_at(121, 1)
ll.insert_at(81, 0)
ll.add_to_beginning(22)
ll.add_to_beginning(56)
ll.add_to_beginning(5)
ll.add_to_beginning(5)
ll.add_to_end(5)
ll.add_to_end(22)
ll.add_to_end(44)
ll.add_to_end(102)
ll.add_to_end(102)
ll.add_to_end(102)
print(ll)

a = CDLinkedList()
b = CDLinkedList()
a.generate(3, 0, 9)
b.generate(3, 0, 9)
print(a)
print(b)
# list2 = ll.generate(3, 0, 10)
# ll.printer()
print(ll.get_length())
# ll.printer()
# # ll.remove_duplicates_2()
# # ll.remove_duplicates()
# ll.printer()
# print(ll.two_pointer(4))
# ll.partitioner(40)
# ll.printer()
# print(sum_of_ll(list1, list2))
print(sum_of_ll(a, b))