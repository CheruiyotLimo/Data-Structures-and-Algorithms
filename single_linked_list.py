class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class LinkedList():
    def __init__(self):
        self.head = None

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
        node = Node(data = data, next = self.head)
        self.head = node
    def add_to_end(self, data):
        node = Node(data = data, next = None)
        itr = self.head
        while itr.next:
            itr = itr.next
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
            if count == index - 1:
                node = Node(data = data, next = itr.next)
                itr.next = node
            itr = itr.next
            count += 1
    
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
        while itr.next:
            if itr.data == data_after:
                node = Node(data = data_to_insert, next = itr.next)
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
            
ll = LinkedList()
ll.add_to_beginning(6)
ll.add_to_beginning(12)
ll.add_to_beginning(87)
ll.add_to_end(34)
ll.insert_at(712, 0)
ll.insert_at(526, 3)
ll.insert_at(96, 4)
ll.remove_at(2)
ll.insert_datalist(list = [21, 56, 77, 89])
ll.insert_after_value(data_after = 34, data_to_insert = 109)
ll.remove_by_value(data = 34)
ll.print()
ll.get_length()
