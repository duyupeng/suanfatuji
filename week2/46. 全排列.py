class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        stack = []
        res = []
        status = [False for i in nums]

        def dfs(status, stack, res):
            if len(stack) == len(nums):
                res.append(stack[:])
                return

            for i, j in enumerate(nums):
                if not status[i]:
                    status[i] = True
                    stack.append(j)
                    dfs(status, stack, res)
                    stack.pop()
                    status[i] = False

        dfs(status, stack, res)
        return res