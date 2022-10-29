  
class Node():
    def __init__(self, prev, data, next):
        self.data = data
        self.prev = None
        self.next = None
    
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
            itr = itr.next
            if itr == self.tail:
                break
        print(llstr)
        return

    def add_to_beginning(self, data):
        if not self.head:
            node = Node(prev=None, data=data, next=None)
            self.head = node
            self.tail = node
            self.head.prev = self.tail
            self.head.next = node      
        else:
            node = Node(prev=self.tail, data=data, next=self.head)
            self.head.prev = node
            self.head = node
            self.tail.next = node
        return
    
    def add_to_end(self, data):
        itr = self.head
        while itr:
            if itr.next == self.head:
                node = Node(prev=self.tail, data=data, next=self.head)
                self.tail.next = node
                self.tail = node
                self.head.prev = self.tail
            itr = itr.next
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
            if itr == self.tail:
                break
        return count    

    def insert_at(self, data, location):
        if location == 0:
            self.add_to_beginning(data=data)
        if location == self.get_length():
            self.add_to_end(data=data)
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

ll = CDLinkedList()
# ll.create(12)
ll.add_to_beginning(5)
ll.insert_at(121, 0)
ll.insert_at(81, 0)
# ll.add_to_beginning(22)
ll.printer()
print(ll.get_length())
