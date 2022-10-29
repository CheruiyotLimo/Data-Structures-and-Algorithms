

class Node():
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def print(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
    
    def add_to_beginning(self, data):
        if not self.head:
            node = Node(prev = None, data = data, next = None)
            self.head = node
        else:
            node = Node(prev = None, data = data, next = self.head)
            # node.next = self.head
            self.head.prev = node
            self.head = node
    def add_to_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(prev = itr.data, data = data, next = None)
        itr.next = node    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        print(count)
        return count

    def insert_at(self, data, index):
        # node = Node(data = data, next = )
        if index == 0:
            self.add_to_beginning(data = data)
        if index == self.get_length():
            self.add_to_end(data = data)
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
            if count == index - 1:
                node = Node(prev = itr.data, data = data, next = itr.next)
                itr.next = node
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index Error")
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def insert_datalist(self, list):
        # self.head = None
        for data in list:
            self.add_to_end(data = data)

    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(prev = itr.data, data = data_to_insert, next = itr.next)
                itr.next = node
            itr = itr.next

    def remove_by_value(self, data):
    # Remove first node that contains data
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                new_count = count - 1
                break
            itr = itr.next
            count += 1
        itr = self.head
        while itr:
            if new_count == 0:
                itr.next = itr.next.next
                break
            new_count -= 1
            itr = itr.next
            
    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        itr = self.head
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + "-->"
            itr = itr.next
        print(dllstr)
        return
            

    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        itr = self.head
        bdllstr = ""
        while itr.next:
            itr = itr.next
        print(itr.data)
        print(type(itr))
        while itr.prev:
            print(itr.prev.prev)
            bdllstr + str(itr.data) + "-->"
            itr = itr.prev
            print(bdllstr)

        print(bdllstr)
        return
        
dll = DoubleLinkedList()
dll.add_to_beginning(6)
dll.add_to_beginning(12)
dll.add_to_beginning(87)
# dll.add_to_end(34)
# dll.insert_at(712, 0)
# dll.insert_at(526, 3)
# dll.insert_at(96, 4)
# dll.remove_at(2)
# dll.insert_datalist(list = [21, 56, 77, 89])
# dll.insert_after_value(data_after = 34, data_to_insert = 109)
# dll.remove_by_value(data = 34)
dll.print()
# dll.print_forward()
# dll.print_backward()