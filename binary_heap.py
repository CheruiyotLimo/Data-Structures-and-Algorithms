
class BinaryHeap:
    def __init__(self, size) -> None:
        self.max_size = size + 1
        self.cust_list = [None] * (size+1)
        self.heap_size = 0

def peek(root):
    if not root:
        return
    return root.cust_list[1]

def size_of_heap(root):
    if not root:
        return
    return root.heap_size

def heapify(root, index, type):
    if index <= 1:
        return
    parent_index = int(index/2)
    if type == "Min":
        if root.cust_list[index] < root.cust_list[parent_index]:
            temp = root.cust_list[parent_index]
            root.cust_list[parent_index] = root.cust_list[index]
            root.cust_list[index] = temp
        heapify(root, parent_index, "Min")
    elif type == "Max":
        if root.cust_list[index] > root.cust_list[parent_index]:
            temp = root.cust_list[parent_index]
            root.cust_list[parent_index] = root.cust_list[index]
            root.cust_list[index] = temp
        heapify(root, parent_index, "Max")
    
def level_order_traversal(root):
    if not root:
        return
    for i in range(1, root.heap_size+1):
        print(root.cust_list[i])

def insert_node_min(root, node, heap_type):
    if root.heap_size + 1 == root.max_size:
        return "The Binary Heap is full."
    root.cust_list[root.heap_size+1] = node
    root.heap_size += 1
    heapify(root, root.heap_size, heap_type)
    return "Done"

bh = BinaryHeap(6)
insert_node_min(bh, 10, "Min")
insert_node_min(bh, 5, "Min")
insert_node_min(bh, 23, "Min")
insert_node_min(bh, 18, "Min")
insert_node_min(bh, 2, "Min")
insert_node_min(bh, 3, "Min")
level_order_traversal(bh)
