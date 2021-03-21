class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def trackback(cur, i, nums):
            if i == n:
                res.append(cur)
                return
            trackback(cur + [nums[i]], i + 1, nums)
            trackback(cur, i + 1, nums)

        trackback([], 0, nums)
        return res