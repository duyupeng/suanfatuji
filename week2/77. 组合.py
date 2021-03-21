class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack = []

        def dfs(depth, stack, res):
            if len(stack) == k:
                res.append(stack[:])

            for i in range(depth, n + 1):
                stack.append(i)
                dfs(i + 1, stack, res)
                stack.pop()

        dfs(1, stack, res)
        return res