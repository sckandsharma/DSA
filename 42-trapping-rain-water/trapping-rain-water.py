class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        n = len(height)
        stack = []

        for i in range(0,n):
            while len(stack) != 0 and height[i] > height[stack[-1]]:

                idx = stack[-1]
                stack.pop()

                if len(stack) == 0:
                    break
                
                left_idx = stack[-1]

                water += (min(height[i],height[left_idx]) - height[idx]) * (i-left_idx-1)

            stack.append(i)

        return water

        