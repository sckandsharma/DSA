class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq_map = {}
        
        #stored everything in the dictianory 
        for ch in s:
            freq_map[ch] = freq_map.get(ch,0) + 1

        #now check which ch has the freq 1

        for i in range(len(s)):
            if freq_map[s[i]] == 1:
                return i

        return -1

        
        