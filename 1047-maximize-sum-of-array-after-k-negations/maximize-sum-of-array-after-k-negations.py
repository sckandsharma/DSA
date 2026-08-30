class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = 0

        while i < n and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1

        res = sum(nums)
        min_value = min(nums)

        if k % 2 == 0:
            return res 
        
        else:
            res -= 2*min_value

        return res
       


        