
class DisjointSet:
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find_element(self, item):
        if self.parent[item] == item:
            return item
        return self.find_element(self.parent[item])

    def union(self, x, y):
        x_root = self.find_element(x)
        y_root = self.find_element(y)
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
