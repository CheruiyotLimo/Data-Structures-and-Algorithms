

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

def get_height(root):
    return root.height

def balance(root):
    if not root:
        return
    return (root.left.get_height()-root.right.get_height())

def right_rotate(unbal_root):
    new_root = unbal_root.left
    unbal_root.right = unbal_root.left.right
    new_root.right = unbal_root
    new_root.height = new_root.get_height()
