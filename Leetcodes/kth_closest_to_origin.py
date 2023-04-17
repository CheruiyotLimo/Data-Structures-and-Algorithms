import math
import heapq

class Solution():
    def calc_distance(self, point1):
        total1 = (point1[0]-point1[1])**2

        return math.sqrt(total1)

    def sort_results(self, elements):
        for i in range(1, len(elements)):
            anchor = elements[i]
            j = i - 1
            while j >= 0 and anchor < elements[j]:
                elements[j + 1] = elements[j]
                j -= 1
            elements[j+1] = anchor
        return elements

    def closest_to_origin(self, points, k):
        result = []
        for i in range(len(points)):
            dist = self.calc_distance(points[i])
            result.append([points[i], dist])
        result = self.sort_results(result)
        return result[:k]

    def closest_to_origin_with_heap(self, points, k):
        heap = []
        for i in range(len(points)):
            dist = self.calc_distance(points[i])
            heapq.heappush(heap, (dist, points[i]))
        results = []
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        return results

sl = Solution()
print(sl.closest_to_origin_with_heap([[3,3],[5,-1],[-2,4]], k = 2))