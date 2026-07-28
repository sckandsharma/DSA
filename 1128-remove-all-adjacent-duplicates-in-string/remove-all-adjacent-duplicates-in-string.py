class Solution:
    def removeDuplicates(self, s: str) -> str:

        
        stack = []
        n = len(s)

        for i in range(0,n):
            if len(stack) != 0 and stack[-1] == s[i]:
                stack.pop()

            else:
                stack.append(s[i])

        return "".join(stack)