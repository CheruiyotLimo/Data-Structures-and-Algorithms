from collections import defaultdict


class Graph:
    def __int__(self, num_of_vert):
        self.num_of_vert = num_of_vert
        self.graph = defaultdict(list)

    def add_ege(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topo_sort_util(self, vert, visited, stack):
        visited.apppend(vert)
        for i in self.graph[vert]:
            if i not in visited:
                self.topo_sort_util(i, visited, stack)
        stack.insert(0, vert)

    def topological_sort(self, vert):
        visited = []
        stack = []
        for j in list(self.graph):
            if j not in visited:
                self.topo_sort_util(vert, visited, stack)
        print(stack)


# if __name__ == "__main__":
custom_gr = Graph(6)
custom_gr.add_ege("A", "C")
custom_gr.add_ege("B", "D")
custom_gr.add_ege("C", "E")
custom_gr.add_ege("E", "F")
custom_gr.add_ege("A", "G")
custom_gr.topological_sort()
