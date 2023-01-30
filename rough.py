from collections import defaultdict, deque
import heapq
x = defaultdict(list)
x["a"] = [100]
x["b"] = [250]
x["c"] = [135]

y = []

for i in x:
    y.append(x[i][0])

heapq.heapify(y)
# print(heapq.heappop(y))
print(y)
