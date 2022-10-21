class UnionFind:
    def __init__(self):
        self.root = {}
        self.sz = {}
        self.count = 1

    def find(self, a):
        if a not in self.root:
            self.root[a] = a
            self.sz[a] = 1
        while self.root[a] != a:
            self.root[a] = self.root[self.root[a]] # include this line for path compression
            a = self.root[a]
        return a
            
    def union(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        if roota != rootb:
            self.root[roota] = self.root[rootb]
            self.sz[rootb] += self.sz[roota]
            self.count = max(self.count, self.sz[rootb])
            
    # compress tree according to size
    def union2(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.sz[root_x] < self.sz[root_y]:
                self.father[root_x] = self.father[root_y]
                self.sz[root_y] += self.sz[root_x]
                self.count = max(self.count, self.sz[root_y])
            else:
                self.father[root_y] = self.father[root_x]
                self.sz[root_x] += self.sz[root_y]
                self.count = max(self.count, self.sz[root_x])
                