class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # array nums -> array output 
        #       output[i] is product of all elements of nums except nums[i]

        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i!=j:
                    product = product * nums[j]
            output.append(product)
        return output