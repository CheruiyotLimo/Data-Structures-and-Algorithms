class TreeNode():
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def get_level(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent
        return count

    # def checks_children(self):
    #     prefix = "  "
    #     if self.children:
    #         for child in self.children:
    #             print(prefix + child.data)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
                



el = TreeNode("Electronics")
phone = TreeNode("Phones")
books = TreeNode("Books")
el.add_child(books)
el.add_child(phone)
oppo = TreeNode("Oppo")
phone.add_child(TreeNode("iPhone"))
phone.add_child(TreeNode("Samsung"))
phone.add_child(TreeNode("Pixel"))
phone.add_child(oppo)
# el.add_child(phone)
el.print_tree()
print(oppo.get_level())
print(phone.get_level())
# print(oppo.parent.parent.parent.data)