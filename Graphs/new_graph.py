

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
    
    # For an unweighted undirectional graph
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
        
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.g_dict.keys() and vertex2 in self.g_dict.keys():
            try:
                self.g_dict[vertex1].remove(vertex2)
                self.g_dict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.g_dict.keys():
            del self.g_dict[vertex]
            for key in self.g_dict.keys():
                if vertex in self.g_dict[key]:
                    self.g_dict[key].remove(vertex)
            return True
        return False
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:                    #Aptly named, best implemented using a queue.
            deq = queue.pop(0)
            print(deq)
            for i in self.g_dict[deq]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            val = stack.pop()
            print(val)
            for i in self.g_dict[val]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)
        
                
cust_graph = {
    "A": ["B"],
    "B": ["A"],
    "C": [],
    "D": []
}
gr = Graph(cust_graph)
# gr.add_edge("A", "E")
gr.add_vertex("E")
print(gr.add_edge("A", "E"))
print(gr.add_edge("A", "D"))
print(gr.add_edge("C", "D"))
print(gr.add_edge("C", "B"))
print(gr.add_edge("D", "E"))
# print(gr.remove_edge("A", "B"))
# print(gr.remove_vertex("A"))
print(gr)
# gr.bfs("A")
gr.dfs("A")