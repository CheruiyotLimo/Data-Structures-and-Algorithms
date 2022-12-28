from collections import defaultdict


class Graph:
    def __init__(self, num_of_vert):
        self.num_of_vert = num_of_vert
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topo_sort_util(self, vert, visited, stack):
        visited.append(vert)
        for i in self.graph[vert]:
            if i not in visited:
                self.topo_sort_util(i, visited, stack)
        stack.insert(0, vert)

    def topological_sort(self):
        visited = []
        stack = []
        for j in list(self.graph):
            if j not in visited:
                self.topo_sort_util(j, visited, stack)
        print(stack)


# if __name__ == "__main__":
custom_gr = Graph(6)
custom_gr.add_edge("A", "C")
custom_gr.add_edge("B", "D")
custom_gr.add_edge("C", "E")
custom_gr.add_edge("E", "F")
custom_gr.add_edge("A", "G")
custom_gr.topological_sort()
