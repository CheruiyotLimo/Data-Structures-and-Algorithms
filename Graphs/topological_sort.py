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

    def cycle_checker(self):
        visited = []
        stack = []
        for key in self.graph:
            if key not in visited:
                if self.dfs(key, list(), visited, stack):
                    return True
        return False

    def dfs(self, vert, path, visited, stack):
        path.append(vert)
        visited.append(vert)
        for i in self.graph[vert]:
            if i == vert:
                continue
            if i in path:
                return True
            if i not in visited and self.dfs(i, path, visited, stack):
                return True
        path.pop()
        return False


# if __name__ == "__main__":
custom_gr = Graph(6)
custom_gr.add_edge("A", "C")
custom_gr.add_edge("B", "D")
custom_gr.add_edge("C", "E")
# custom_gr.add_edge("C", "A")
custom_gr.add_edge("E", "F")
# custom_gr.add_edge("E", "A")
custom_gr.add_edge("A", "G")
custom_gr.topological_sort()
print(custom_gr.graph)
print(custom_gr.cycle_checker())