from collections import defaultdict, deque
import heapq
x = [
    ["A", 3, 2],
    ["B", 4, 1]
]


x.sort(key=lambda x: x[1])

print(x)