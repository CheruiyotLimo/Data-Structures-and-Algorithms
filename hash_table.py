
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


#Conflict resolution technique:
# 1. Direct chaining - Use a linked list at each index so that subsequent values will be added as another node to the
#                       linked list. Good cause hash table never gets full but bad when n is large as insertions, 
#                       searching will take O(n) hence beating the purpose of a hash function.

# 2. Open addressing - Linear probing - Here if a certain hash value(2) is already filled, we look for the next 
#                                       available hash value using 2 + 1, 2 + 2, 2 + 3....2+n
#
#                      Quadratic probing - If a cerain hash value (2) is already filled, we look for the next 
#                                          available hash value using 2 + 1^2, 2 + 2^2, 2 + 3^2.....2+n^2
#
#                      Double hashing - If a hash-value(2) is filled, then we implement a second hash function to
#                                       generate a new hash-value(4) then um them i.e. 2+4 = 6. If the hash value sum 
#                                       is filled, then we double the result of the 2nd hash function i.e 2 + (1*4), 
#                                       2 + (2*4), 2 + (3*4).... 2+(n*4)
        # Is the mainstay preferrred methof od conflict resolution and becomes evenmore ideal when there is a 
        # fixed number of values to be hashed. May grow slower if there will be lots of deletions but averagely
        # maintain O(1) complexity. 

ht = HashTable()
# ht.hash_function("march 24")
ht["march 4"] = 133
ht["april 5"] = 142
ht["september 5"] = 3
ht["march 23"] = 57
ht["march 24"] = 1245
ht["march 24"] = 90
# del ht["april 5"]
print(ht.arr)
