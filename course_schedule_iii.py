
class Solution:
    def length_gen(self, courses, index):
        courses.sort(key=lambda x: x[index])
        results = []
        days_spent = 0
        for j in range(len(courses)):
            if days_spent + courses[j][0] <= courses[j][1]:
                results.append(courses[j])
                days_spent += courses[j][0]
        return len(results)

    def scheduleCourse(self, courses: list[list[int]]) -> int:
        return max(self.length_gen(courses, 0), self.length_gen(courses, 1))

courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]

s = Solution()
print(s.scheduleCourse(courses))