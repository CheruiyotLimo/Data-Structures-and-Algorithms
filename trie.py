

class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.end_of_string = False
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert_string(self, word):
        curr = self.root
        for i in word:
            node = curr.children.get(i)
            if node == None:
                node = TrieNode()
                curr.children.update({i: node})
            curr = node
        curr.end_of_string = True
        print("Success!")

tr = Trie()
tr.insert_string("ALL")
tr.insert_string("A0L")