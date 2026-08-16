class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        n = len(s)
        left = 0
        right = 0
        maxi = 0

        while right<n:
            ch = s[right]

            if ch in seen:

                if seen[ch] >= left:
                    left = seen[ch] + 1

            maxi = max(maxi,right-left+1)

            seen[ch] = right
            right+=1

        return maxi

                
        