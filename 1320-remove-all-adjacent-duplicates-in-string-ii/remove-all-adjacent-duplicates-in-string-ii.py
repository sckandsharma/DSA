class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        n = len(s)

        for i in range(0,n):
            if len(stack) == 0:
                stack.append([s[i],1])

            else:
                if stack[-1][0] == s[i]:
                    stack[-1][1] += 1

                    if stack[-1][1] == k:
                        stack.pop()

                else:
                    stack.append([s[i],1])  

        ans = []
        
        for i in range(len(stack)):
            ch = stack[i][0]
            count = stack[i][1]

            ans.append(ch*count)

        return "".join(ans)

            
        