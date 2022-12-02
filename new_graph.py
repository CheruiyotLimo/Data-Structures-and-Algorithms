

class Graph:
    def __init__(self, g_dict=None) -> None:
        if not g_dict:
            g_dict = {}
        self.g_dict = g_dict
    
    def __str__(self) -> str:
        for vert in self.g_dict:
            print(f"{str(vert)}: {self.g_dict[vert]}")
        return "End"
    
    def add_vertex(self, vertex):
        if vertex not in self.g_dict.keys():
            self.g_dict[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.g_dict.keys() and vertex2 in self.g_dict.keys():
            if vertex1 in self.g_dict[vertex2] and vertex2 in self.g_dict[vertex1]:
                return "Already connected"
            # elif vertex2 not in self.g_dict[vertex1]:
            #     self.g_dict[vertex1].append(vertex2)
            # elif vertex1 not in self.g_dict[vertex2]:
            #     self.g_dict[vertex2].append(vertex1)
            else:
                self.g_dict[vertex1].append(vertex2)
                self.g_dict[vertex2].append(vertex1)
            return True
        return False

cust_graph = {
    "A": ["B",],
    "B": ["A",],
    "C": [],
    "D": []
}
gr = Graph(cust_graph)
# gr.add_edge("A", "E")
gr.add_vertex("E")
print(gr.add_edge("A", "C"))
print(gr.add_edge("C", "D"))
print(gr)
