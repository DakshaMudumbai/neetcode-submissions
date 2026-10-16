class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = dict()
        for i in range(len(nums)):
            missing_val = target - nums[i]
            if missing_val in tracker: 
                return [tracker[missing_val], i]
            tracker[nums[i]] = i
            

