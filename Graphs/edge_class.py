import heapq


class Edge:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.min_dist = float("inf")

    def __lt__(self, other):
        return self.min_dist < other.min_dist

    def add_edge(self, weight, destination):
        edge = Edge(weight, self, destination)
        self.neighbours.append(edge)


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate_distance(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbours:
                start = edge.start
                end = edge.end
                new_distance = start.min_dist + edge.weight
                if new_distance < end.min_dist:
                    end.min_dist = new_distance
                    end.predecessor = start
                    heapq.heappush(self.heap, end)
            actual_vertex.visited = True
        # return end.min_dist

    def get_shortest_path(self, vertex):
        print(f"The shortest distance to {vertex.name} is {vertex.min_dist}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor


# creating the individual nodes
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")

# adding the edges to nodes
node_A.add_edge(6, node_B)
node_A.add_edge(9, node_D)
node_A.add_edge(10, node_C)

node_B.add_edge(16, node_E)
node_B.add_edge(13, node_F)
node_B.add_edge(5, node_D)

node_C.add_edge(6, node_D)
node_C.add_edge(5, node_H)
node_C.add_edge(21, node_G)

node_D.add_edge(8, node_F)
node_D.add_edge(7, node_H)

node_E.add_edge(8, node_G)

node_F.add_edge(4, node_E)
node_F.add_edge(12, node_G)

node_H.add_edge(2, node_F)
node_H.add_edge(14, node_G)

algo = Dijkstra()
algo.calculate_distance(node_A)
algo.get_shortest_path(node_G)
# print(node_G.min_dist)