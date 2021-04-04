class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        uf = Unionfind()
        row = len(grid)
        col = len(grid[0])
        if not grid:
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':

                    for x, y in [(-1, 0), (0, -1)]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if -1 < tmp_i < row and -1 < tmp_j < col and grid[tmp_i][tmp_j] == '1':
                            dot = i * row + j
                            dot_next = tmp_i * row + tmp_j
                            uf.add(dot)
                            uf.add(dot_next)
                            uf.merge(dot, dot_next)
        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    uf.add(i * row + j)
                    res.add(uf.find(i * row + j))
        return len(res)


class Unionfind():
    def __init__(self):
        self.top = {}

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.top[root_x] = root_y

    def find(self, x):
        root = x
        while self.top[root] != root:
            root = self.top[root]
        while x != root:
            origin_father = self.top[x]
            self.top[x] = root
            x = origin_father
        return root

    def add(self, x):
        if x not in self.top:
            self.top.setdefault(x, x)