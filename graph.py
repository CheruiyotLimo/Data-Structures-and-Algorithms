
class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)
        return

    def get_paths(self, start, end, possible_routes = []):
        possible_routes = possible_routes + [start]
        if start == end:
            return [possible_routes]
        if start in self.graph_dict:
            paths = []
            for dest in self.graph_dict[start]:
                new_paths = self.get_paths(dest, end, possible_routes)
                for p in new_paths:
                    paths.append(p)
            return paths
        else:
            return []
    
    def shortest_possible_path_stops(self, start, end, possible_routes = []):
        '''By number of nodes/stop-overs.'''
        possible_routes = possible_routes + [start]
        if start == end:
            return possible_routes
        if start in self.graph_dict:
            paths = None
            for dest in self.graph_dict[start]:
                shortest_paths = self.shortest_possible_path_stops(dest, end, possible_routes)
                if shortest_paths:
                    if paths is None or len(shortest_paths) < len(paths):
                        paths = shortest_paths
            return paths
        else:
            return []
    # def shortest_possible_path_distance(self, start, end, p =[])

routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
route_graph = Graph(routes)
start = "Mumbai"
end = "New York"
print(route_graph.get_paths(start = start, end = end))
print(f"The shortest path between {start} & {end} is ", route_graph.shortest_possible_path_stops(start = start, end = end))
