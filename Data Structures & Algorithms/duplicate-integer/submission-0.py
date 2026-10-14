from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # take an array, return true if any value appears more than once in the array

        # run through the array, each number gets added to a set, if the set alrdy has the number present, means its a duplicate. return true 

        counter = set()
        for n in nums:
            if n in counter:
                return True
            counter.add(n)
        return False