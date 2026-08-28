class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        n = len(g)
        m = len(s)

        left = 0
        count = 0
        right = 0

        g.sort()
        s.sort()

        while left < n and right < m:
            if g[left] <= s[right]:
                count += 1
                left += 1
            right += 1

        return count
        