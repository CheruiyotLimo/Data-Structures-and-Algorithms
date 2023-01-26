from collections import defaultdict, deque
x = defaultdict(list)
x["a"] = [1, 3, 4]
x["b"] = [1, 3, 4]
x["c"] = [1, 3, 5]

del x["a"]

print(x)