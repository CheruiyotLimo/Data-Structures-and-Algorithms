  
class Node():
    def __init__(self, prev, data, next):
        self.data = data
        self.prev = prev
        self.next = next
    
class CDLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def printer(self):
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
        print(llstr)
        return

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
                # print("ender")
                break
                
            itr = itr.next
            # print("Ender")
    
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

ll = CDLinkedList()
# ll.create(12)
ll.add_to_beginning(5)
ll.add_to_beginning(8)
ll.insert_at(121, 1)
ll.insert_at(81, 0)
ll.add_to_beginning(22)
ll.add_to_beginning(56)
ll.add_to_beginning(35)
ll.add_to_end(102)
ll.printer()
# ll.insert_at(201, 5)
# ll.remove_at(0)
ll.remove_at(7)
ll.printer()

print(ll.get_length())

