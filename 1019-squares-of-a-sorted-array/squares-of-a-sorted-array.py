class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        n = len(nums)
        result = [0]*n
        
        i = 0
        j = n-1

        k = n-1

        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                result[k] = nums[i] * nums[i]
                i += 1
            else:
                result[k] = nums[j] * nums[j]
                j -= 1
            
            k -= 1

        return result
        