class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collect_dict={}
        for i,j in enumerate(nums):
            collect_dict[j]=i
        for i,j in enumerate(nums):
            if target-j in nums[i+1:]:
                return [i,collect_dict.get(target-j)]