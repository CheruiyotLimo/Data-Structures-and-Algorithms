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
        heapq.heappushpop(self.heap, start_vertex)
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

    def get_shortest_path(self, vertex):
        print(f"The shortest distance to {vertex}" is {vertex.min_dist})
        while vertex:
            print(vertex.name, end=" ")
            vertex = vertex.predecessor
            