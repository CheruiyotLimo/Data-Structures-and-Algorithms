from queue import Queue
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

#Implementation using a linked list
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_child(root, data):
    new_node = TreeNode(data)
    if not root:
        root = node
    else:
        qu = queue.Queue2()
        qu.enqueue(root)
        while not qu.isEmpty():
            node = qu.dequeue()
            if node.left and node.right:
                qu.enqueue(node.left)
                qu.enqueue(node.right)
            elif not node.left:
                node.left = new_node
                break
            else:
                node.right = new_node
                break
        return
    
def print_tree(self):
    # spaces = " " * self.get_level() * 3
    print(self.data)
    if self.left:
        self.left.print_tree()
    if self.right:
        self.right.print_tree()
    return

def pre_order_traversal(self):          #Depth-first traversal
    if not self:
        return
    else:
        print(self.data)
        pre_order_traversal(self.left)
        pre_order_traversal(self.right)

def in_order_traversal(root):           ##Depth-first traversal
    if not root:
        return
    else:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)

def post_order_traversal(self):         #Depth-first traversal
    if not self:
        return
    else:
        post_order_traversal(self.left)
        post_order_traversal(self.right)
        print(self.data)

def level_order_traversal(self):      #Breadth first traversal
    if not self:
        return
    else:
        qu = Queue2()
        qu.enqueue(self)
        while not qu.isEmpty():
            node = qu.dequeue()
            if node:
                print(node.data)
                qu.enqueue(node.left)
                qu.enqueue(node.right)

def search(self, data):   #Preferable to use level-order traversal.
    if not self:
        return
    else:
        qu = Queue2()
        qu.enqueue(self)
        while not qu.isEmpty():
            node = qu.dequeue()
            if data == node.data:
                return "Found the data."
            if node.left:
                qu.enqueue(node.left)
            if node.right:
                qu.enqueue(node.right)
        return "Data not found."

def find_max_depth(root):
    if not root:
        return
    else:
        qu = Queue2()
        qu.enqueue(root)
        count = 0
        while not qu.isEmpty():
            count += 1
            node = qu.dequeue()
            if node.left:
                qu.enqueue(node.left)
            if node.right:
                qu.enqueue(node.right)  
        # print(f"{node.data} is the deepest at level {count}")
        return node

    
def del_deepest_node(root):
    if not root:
        return
    else:
        qu = Queue2()
        qu.enqueue(root)
        deepest = find_max_depth(root)
        while not qu.isEmpty():  
            node = qu.dequeue()
            if node is deepest:
                node = None
            else:
                if node.right:
                    if node.right is deepest:
                        node.right = None
                        return
                    else:
                        qu.enqueue(node.right)
                if node.left:
                    if node.left is deepest:
                        node.left = None
                        return
                    else:
                        qu.enqueue(node.left)

def delete_node(root, d_node):    #When deleting a node, if the node has children, or even not,
    if not root:                    #then we replace the node with the deepest node.
        return
    else:
        qu = Queue2()
        qu.enqueue(root)
        while not qu.isEmpty():
            deepest = find_max_depth(root)
            node = qu.dequeue()
            if node.data == d_node:
                del_deepest_node(root)
                node = deepest
                return
            else:
                if node.left.data == d_node:
                    if node.left.data is deepest.data:
                        node.left = None
                        return
                    else:
                        del_deepest_node(root)
                        node.left.data = deepest.data
                        return
                else:
                    if node.left:
                        qu.enqueue(node.left)
                if node.right.data == d_node:
                    if node.right.data is deepest.data:
                        node.right = None
                    del_deepest_node(root)
                    node.right.data = deepest.data
                    return
                else:
                    if node.right:
                        qu.enqueue(node.right)

#Implementation using a python list.
class TreeNode2:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.cust_list = [None] * max_size
        self.last_index = 0
    
    def __str__(self):
        return str(self.cust_list)

    def add_value(self, value):
        if self.last_index + 1 > self.max_size:
            return "The list is full."
        self.cust_list[self.last_index+1] = value
        self.last_index += 1

    def search(self, value):
        for i in  range(len(self.cust_list)):
            if self.cust_list[i] == value:
                return "Item found"
        return "Not in list."\

    def pre_order_traversal(self, index):
        if index > self.last_index+1:
            return
        print(self.cust_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2+1)

    def in_order_traversal(self, index):
        if index > self.last_index+1:
            return
        self.in_order_traversal(index*2)
        print(self.cust_list[index])
        self.in_order_traversal(index*2+1)

    def post_order_traversal(self, index):
        if index > self.last_index+1:
            return
        self.post_order_traversal(index*2)
        self.post_order_traversal(index*2+1)
        print(self.cust_list[index])
    
    def level_order_traversal(self, index):
        if index > self.last_index+1:
            return
        for i in range(index, len(self.cust_list)):
            if self.cust_list[i]:
                print(self.cust_list[i])
    
    def delete_node(self, value):
        for i in range(1, len(self.cust_list)):
            if self.cust_list[i] == value:
                delet = self.cust_list[i]
                self.cust_list[i] = self.cust_list[self.last_index]
                self.cust_list[self.last_index] = None
                self.last_index -= 1
                return delet


el = TreeNode2(10)
el.add_value("Electronics")
el.add_value("Phones")
el.add_value("Books")
el.add_value("iPhone")
el.add_value("Samsung")
# add_child("Electronics")
# add_child("Phones")
# add_child(el, "Books")
# add_child(el, "Iphone")
# add_child(el, "Samsung")
# add_child(el, "City of Thieves")
# add_child(el, "Horror")
# add_child(el, "14 Pro")
# add_child(el, "8 Pro")
# print(find_max_depth(el))
print(el)
# print(el.search("Samsung"))
# el.level_order_traversal(1)
print(el.delete_node("Books"))
# el.level_order_traversal(1)
print(el)



# phone.add_child(TreeNode("Pixel"))
# print(pre_order_traversal(el))
# print(post_order_traversal(el))
# print(in_order_traversal(el))
# del_deepest_node(el)
# delete_node(el, "14 Pro")
# delete_node(el, "Books")
# print(in_order_traversal(el))

# print(level_order_traversal(el))
# print(search(el, "SA"))