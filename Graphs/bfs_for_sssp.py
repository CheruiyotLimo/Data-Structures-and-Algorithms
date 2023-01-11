
class Graph:
    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict

    def bfs(self, start, end) -> list:
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.g_dict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return path


custom_dict = {
    "A": ["B", "C"],
    "B": ["D", "G"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "G": ["F"]
}
g = Graph(custom_dict)
print(g.bfs("A", "F"))
