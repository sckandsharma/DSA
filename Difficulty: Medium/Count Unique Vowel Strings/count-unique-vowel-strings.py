class Solution:
    def vowelCount(self, s):
        #code here
        
        freq = {}
        
        for ch in s:
            
            if ch in "aeiou":
                freq[ch] = freq.get(ch,0) + 1
                
        n = len(freq)
        
        if n == 0:
            return 0
            
        ans = 1
        
        for ch in freq:
            ans *= freq[ch]
            
        for i in range(1,n+1):
            ans *= i
            
        return ans
            
        