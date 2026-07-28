class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array nums, target int, ret indices i & j 
        # where, nums[i] + nums[j] == target && i != j
        # only one pair satisfy 

        seen = {}
        for i, n in enumerate(nums):
            missing_val = target - n 
            if missing_val in seen:
                return [seen[missing_val],i]
            seen[n] = i
