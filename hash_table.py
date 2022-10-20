
class HashTable():
    def __init__(self):

        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def hash_function(self, key):
        tot = 0
        for char in key:
            tot += ord(char)
        print(tot)
        ind = tot % self.MAX
        print(ind)
        return ind
    '''Creates a key-value pair in memory'''
    def __setitem__(self, data, value):
        found = False
        h = self.hash_function(data)
        for ind, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == data:
                self.arr[h][ind] = (data, value)
                found = True
        if not found:
            self.arr[h].append((data, value))
    
    def __getitem__(self, key):
        h = self.hash_function(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]
        
    def __delitem__(self, data):
        h = self.hash_function(data)
        for index, element in enumerate(self.arr[h]):
            if element[0] == data:
                del self.arr[h][index]

ht = HashTable()
# ht.hash_function("march 24")
ht["march 4"] = 133
ht["april 5"] = 142
ht["september 5"] = 3
ht["march 23"] = 57
ht["march 24"] = 1245
ht["march 24"] = 90
del ht["april 5"]
print(ht.arr)
