class Solution:

    def palindromecheck(self, i: int, j: int, s: str):
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:

            left = s[i]
            right = s[j]

            if left != right:
                return self.palindromecheck(i + 1, j, s) or self.palindromecheck(i, j - 1, s)

            i += 1
            j -= 1

        return True