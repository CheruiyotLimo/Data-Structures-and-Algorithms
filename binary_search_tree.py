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

class Queue2():
    def __init__(self):
        self.arr = LLStack()
    
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
        node = Node(data)
        if self.isEmpty():
            node.next = node
            node.prev = node
            self.arr.head = node
            self.arr.tail = node
        else:
            node.next = self.arr.head
            node.prev = self.arr.tail
            self.arr.head.prev = node
            self.arr.head = node
            self.arr.tail.next = node
        return

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        if len(self) == 1:
            x = self.arr.head.prev.data
            self.arr.head = None
            self.arr.tail = None
        else:
            x = self.arr.head.prev.data
            self.arr.tail = self.arr.tail.prev
            self.arr.tail.next = self.arr.head
            self.arr.head.prev = self.arr.tail
        return x

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.arr.head.prev.data

class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, value):
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                return self.left.add_child(value)
            else:
                self.left = BinaryTreeNode(value)
        else:
            if self.right:
                return self.right.add_child(value)
            else:
                self.right = BinaryTreeNode(value)
    
    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        # print(elements)
        return elements

    def find_min(self):
        if self.left is None:   #May need to rule out one edge case(Check AVL)
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def calculate_sum(self):
        count = 0
        for el in self.in_order_traversal():
            count += el
        return count

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def level_order_traversal(self):
        elements = []
        if not self:
            return
        else:
            qu = Queue2()
            qu.enqueue(self)
            while not qu.isEmpty():
                node = qu.dequeue()
                elements.append(node.data)
                if node.left:
                    qu.enqueue(node.left)
                if node.right:
                    qu.enqueue(node.right)
            return elements

    # def delete(self, value): #Not working well.
    #     if value < self.data:
    #         self.left = self.left.delete(value = value)
    #     if value > self.data:
    #         self.right = self.right.delete(value = value)
    #     else:
    #         # if self.left is None and self.right is None:
    #         #     return
    #         if self.right is None:
    #             temp = self.left
    #             self.left = None
    #             return temp
    #         elif self.left is None:
    #             temp = self.right
    #             self.right = None
    #             return temp
    #         min_val = self.right.find_min()
    #         self.data = min_val
    #         self.right = self.right.delete(min_val)
    #     return self
    def delete_node(self, node_value):
        if not self:
            return self
        elif node_value < self.data:
            self.left = self.left.delete_node(node_value)
        elif node_value > self.data:
            self.right = self.right.delete_node(node_value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.right.find_min()
            self.data = temp
            self.right = self.right.delete_node(temp)
            return self

def tree_builder(numbers):
    root = BinaryTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    return root


x = tree_builder([17, 4, 1, 20, 9, 23, 18, 34])
print(x)
# print(["In order: "],  x.in_order_traversal())
# # print(x.find_min())
# # print(x.find_max())
# # print(x.calculate_sum())
# print(["Pre_order: "], x.pre_order_traversal())
# print(["Post-order: "], x.post_order_traversal())
# # print(x.delete(4))
# print(["In order: "],  x.in_order_traversal())
print("Level Order: ",  x.level_order_traversal())
print(x.delete_node(23))
print("Level Order: ",  x.level_order_traversal())
