self.num_islands -= 1


def find(self, x):
    root = x
    while root != self.top[root]:
        root = self.top[root]
    while x != root:
        oringe_parent = self.top[x]
        self.top[x] = root
        x = oringe_parent
    return root


def add(self, x):
    if x not in self.topclass Solution:


def findCircleNum(self, isConnected: List[List[int]]) -> int:
    uf = Unionfind()
    m = len(isConnected)
    for i in range(m):
        uf.add(i)
        for j in range(i):
            if isConnected[i][j]:
                uf.merge(i, j)
    return uf.num_islands


class Unionfind:
    def __init__(self):
        self.top = {}
        self.num_islands = 0

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.top[root_x] = root_y
        :
        self.top.setdefault(x, x)
        self.num_islands += 1