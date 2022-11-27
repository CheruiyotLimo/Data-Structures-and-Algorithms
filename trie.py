

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
    
    def search(self, word):
        curr = self.root
        for i in word:
            node = curr.children.get(i)
            if node == None:
                return "False"
            curr = node
        if curr.end_of_string == False:
            return False
        return True

def delete_string(root, word, index):
    ch = word[index]
    curr = root.children.get(ch)
    to_be_del = False

    if len(curr.children) > 1:
        delete_string(curr, word, index+1)
        return False
    if index == len(word)-1:
        if len(curr.children) >= 1:
            curr.end_of_string = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if curr.end_of_string == True:
        delete_string(curr, word, index+1)
        return False

    to_be_del = delete_string(curr, word, index+1)
    if to_be_del == True:
        root.children.pop(ch)
        return True
    return False

tr = Trie()
tr.insert_string("A0L")
tr.insert_string("ALL")
tr.insert_string("ALLP")
delete_string(tr.root, "ALL", 0)
print(tr.search("ALL"))