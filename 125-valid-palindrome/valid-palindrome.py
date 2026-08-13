class Solution:

    def isAlphaNumericCharacter(self,c):
        return("a" <= c <= "z") or ("A" <= c <= "Z" ) or ("0" <= c <= "9")
        
        
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1 

        while i < j:
            
            c1 = s[i]
            c2 = s[j]

            if not self.isAlphaNumericCharacter(c1):
                i += 1
                continue
            
            if not self.isAlphaNumericCharacter(c2):
                j -= 1
                continue

            if c1.lower() != c2.lower():
                return False

            i += 1
            j -= 1

        return True 
                