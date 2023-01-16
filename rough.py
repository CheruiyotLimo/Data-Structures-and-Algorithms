import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        # if nums:
        heapq.heapify(nums)
        self.nums = nums

list1 = [5, 7, 9, 1, 3]
kl = KthLargest(3, list1)
print(heapq.heappop(kl.nums))
print(heapq.heappop(kl.nums))
# # heapq.heapify(list1)
# print(list1)
# # print(heapq.heappush(list1, 10))
# # print(heapq.heappush(list1, 4))
# print(list1)
# heapq.heappop(list1)
# heapq.heappop(list1)
# heapq.heappop(list1)
# print(list1)
print(kl.nums)