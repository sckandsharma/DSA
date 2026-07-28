class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        n = len(heights)
        ans = [0]*n
        stack = []

        for i in range(0,n):
            
            while len(stack) != 0 and stack[-1][0] < heights[i]:
                ans[stack[-1][1]] += 1
                stack.pop()

            if len(stack) != 0:
                ans[stack[-1][1]] += 1

            stack.append([heights[i],i])

        return ans
        

        

                

            
        