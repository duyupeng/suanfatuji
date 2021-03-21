def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    stack = []
    res = []
    status = [False for i in range(len(nums))]

    def dfs(status, stack, res):
        if len(stack) == len(nums):
            res.append(stack[:])
            return

        for i, j in enumerate(nums):
            if not status[i]:
                if i > 0 and nums[i] == nums[i - 1] and not status[i - 1]:
                    continue
                status[i] = True
                stack.append(j)
                dfs(status, stack, res)
                stack.pop()
                status[i] = False

    nums.sort()
    dfs(status, stack, res)
    return res