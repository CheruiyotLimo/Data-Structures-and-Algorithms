import disjoint_set as dst

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.mst = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, s, d, w):
        for s, d, w in self.mst:
            print("%s - %s: %s" % (s, d, w))

    def kruskal_algorithm(self):
        i, e = 0, 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.vertices - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find_element(s)
            y = ds.find_element(d)
            if x != y:
                e += 1
                self.mst.append([s, d, w])
                ds.union(x, y)
        self.print_solution(s, d, w)


g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")

g.add_edge("A", "B", 5)
g.add_edge("A", "C", 13)
g.add_edge("A", "E", 15)
g.add_edge("B", "A", 5)
g.add_edge("B", "C", 10)
g.add_edge("B", "D", 8)
g.add_edge("C", "A", 13)
g.add_edge("C", "B", 10)
g.add_edge("C", "E", 20)
g.add_edge("C", "D", 6)
g.add_edge("D", "B", 8)
g.add_edge("D", "C", 6)
g.add_edge("E", "A", 15)
g.add_edge("E", "C", 20)

g.kruskal_algorithm()