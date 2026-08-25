class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        max_index = 0

        for i in range(0,n):
            
            if i > max_index:
                return False
            else:
                max_index = max(max_index,i+nums[i])

        return True