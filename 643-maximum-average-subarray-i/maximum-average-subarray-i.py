class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        total = 0
        maxi = float("-inf")
        left = 0

        for right in range(left,n):
            total += nums[right]
            
            if right >= k:
                total -= nums[left]
                left += 1
            
            if right >= k-1:
                maxi = max(total,maxi)
        return maxi/k
                


        