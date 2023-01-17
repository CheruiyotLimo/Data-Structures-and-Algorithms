import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        heapq.heapify(self.heap)

    def findMedian(self) -> float:
        m_index = len(self.heap)//2
        repl = []
        if len(self.heap)%2 == 0:      # Even number
            for _ in range(m_index):
                y = heapq.heappop(self.heap)
                repl.append(y)
            z = heapq.heappop(self.heap)
            repl.append(z)
            for i in repl:
                heapq.heappush(self.heap, i)
            return (y+z)/2
        else:       # Odd number
            for _ in range(m_index+1):
                x = heapq.heappop(self.heap)
                repl.append(x)
            for i in repl:
                heapq.heappush(self.heap, i)
            return x

# Trying to use a sorted list.
class MedianFinder2:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        qs = sorted(self.heap)

    def findMedian(self) -> float:
        qs = sorted(self.heap)
        m_index = len(self.heap)//2
        if len(qs) % 2 == 0:
            return (qs[m_index]+qs[m_index-1])/2
        else:
            return qs[m_index]

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.heap)
print(mf.findMedian())