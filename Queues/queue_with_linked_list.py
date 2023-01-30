#Need to import LL
from ..double_linked_list import DoubleLinkedList
class Queue2():
    def __init__(self):
        self.arr = DoubleLinkedList()
    
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
        # node = Node(data)
        # if self.isEmpty():
        #     node.next = node
        #     node.prev = node
        #     self.arr.head = node
        #     self.arr.tail = node
        # else:
        #     node.next = self.arr.head
        #     node.prev = self.arr.tail
        #     self.arr.head.prev = node
        #     self.arr.head = node
        #     self.arr.tail.next = node
        # return
        return self.arr.add_to_end(data)

    def dequeue(self):
        # if self.isEmpty():
        #     return "The queue is empty"
        # x = self.arr.head.prev.data
        # self.arr.tail = self.arr.tail.prev
        # self.arr.tail.next = self.arr.head
        # self.arr.head.prev = self.arr.tail
        # return x
        return self.arr.remove_at(0)

    def peek(self):
        if self.arr.head == None:
            return "The queue is empty"
        return self.arr.tail

qu = Queue2()
qu.enqueue(5)
qu.enqueue(12)
qu.enqueue(3)
qu.enqueue(89)
print(qu)