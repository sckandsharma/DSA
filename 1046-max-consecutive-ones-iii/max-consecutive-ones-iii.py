class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0

        for right in range(0,n):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            ans = max(ans,right-left+1)

        return ans 