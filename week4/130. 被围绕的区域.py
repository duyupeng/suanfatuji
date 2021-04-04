class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        uf = Unionfind()
        row = len(board)
        col = len(board[0])
        dummy = row * col
        uf.add(dummy)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        uf.add(i * col + j)
                        uf.merge(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                dot = i * col + j
                                dot_next = (i + x) * col + (j + y)
                                uf.add(dot)
                                uf.add(dot_next)
                                uf.merge(dot, dot_next)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    uf.add(i * col + j)
                    if uf.find(dummy) != uf.find(i * col + j):
                        board[i][j] = "X"


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