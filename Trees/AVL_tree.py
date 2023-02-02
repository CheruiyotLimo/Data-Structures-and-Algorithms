

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

class AVLTree():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


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
    empty = []
    if not self:
        return
    else:
        qu = Queue2()
        qu.enqueue(self)
        while not qu.isEmpty():
            node = qu.dequeue()
            if node:
                # print(node.data)
                empty.append(node.data)
                qu.enqueue(node.left)
                qu.enqueue(node.right)
        return empty

def get_height(root):
    if not root:
        return 0
    return root.height

def balance(root):
    if not root:
        return 0
    return (get_height(root.left)-get_height(root.right))

def right_rotate(unbal_root):
    new_root = unbal_root.left
    unbal_root.left = unbal_root.left.right
    new_root.right = unbal_root
    unbal_root.height = 1 + max(get_height(unbal_root.left), get_height(unbal_root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root

def left_rotate(unbal_root):
    new_root = unbal_root.right
    unbal_root.right = unbal_root.right.left
    new_root.left = unbal_root
    unbal_root.height = 1 + max(get_height(unbal_root.left), get_height(unbal_root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root

def add_node(root, node_value):
    if not root:
        return AVLTree(node_value)
    elif node_value < root.data:
        root.left = add_node(root.left, node_value)
    else:
        root.right = add_node(root.right, node_value)
        # print("l")
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    bal = balance(root)
    
    if bal > 1 and node_value < root.left.data:    #Left-left condition
        return right_rotate(root)
    if bal > 1 and node_value > root.left.data:    #Left-right condition
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if bal < -1 and node_value > root.right.data:    #Right-right condition
        return left_rotate(root)
    if bal < -1 and node_value < root.right.data:    #Right-left condition
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

def min_val(root):
    if not root or not root.left:
        return root
    return min_val(root.left)

def delete_node(root, node_value):    #Some edge scenarios seem like they do not work
    if not root:
        return root
    elif node_value < root.data:
        root.left = delete_node(root.left, node_value)
    elif node_value > root.data:
        root.right = delete_node(root.right, node_value)
    else:
        # if root.left is None and root.right is None:
        #     return
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return 
        temp = min_val(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
        return root
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    bal = balance(root)
    if bal > 1 and balance(root.left) >= 0:    #Left-Left condition
        return right_rotate(root)
    if bal < -1 and balance(root.right) <= 0:    #Right-right condition
        return left_rotate(root)
    if bal > 1 and balance(root.left) < 0:       #Left-right condition
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if bal < -1 and balance(root.right) < 0:     #Right-left condition
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

av = AVLTree(5)
av = add_node(av, 10)
av = add_node(av, 20)
av = add_node(av, 30)
av = add_node(av, 40)
av = add_node(av, 50)
av = add_node(av, 60)
av = add_node(av, 70)
av = add_node(av, 55)
print(level_order_traversal(av))
av = delete_node(av, 50)
print(level_order_traversal(av))
av = delete_node(av, 40)
print(level_order_traversal(av))
av = delete_node(av, 70)
print(level_order_traversal(av))
# in_order_traversal(av)
# print(get_height(av.right))