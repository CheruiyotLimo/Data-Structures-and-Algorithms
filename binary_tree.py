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
        qu = Queue2()
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



# phone = TreeNode("Phones")
# books = TreeNode("Books")
# el.left = phone
# el.right = books
# # iphone = TreeNode("iPhone")
# # sams = TreeNode("Samsung")
# phone.add_child("iPhone")
# phone.add_child("Samsung")
# phone.add_child(TreeNode("Oppo"))
    
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

def delete_node(root, d_node):    #When deleting a node, if the node has children, then we replace the node with the deepest node.
    if not root:
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
                    del_deepest_node(root)
                    node.left.data = deepest.data
                    return
                else:
                    if node.left:
                        qu.enqueue(node.left)
                if node.right.data == d_node:
                    del_deepest_node(root)
                    node.right.data = deepest.data
                    return
                else:
                    if node.right:
                        qu.enqueue(node.right)




el = TreeNode("Electronics")
add_child(el, "Phones")
add_child(el, "Books")
add_child(el, "Iphone")
add_child(el, "Samsung")
add_child(el, "City of Thieves")
add_child(el, "Horror")
add_child(el, "14 Pro")
print(find_max_depth(el))



# phone.add_child(TreeNode("Pixel"))
# print(pre_order_traversal(el))
# print(post_order_traversal(el))
# print(in_order_traversal(el))
# del_deepest_node(el)
delete_node(el, "Books")
print(in_order_traversal(el))

# print(level_order_traversal(el))
# print(search(el, "SA"))