class Solution:
    def reverseWords(self, s: str) -> str:

        arr = list(s)
        n = len(s)

        start = 0

        while start < n:
            end = start

            while end < n and arr[end] != " ":
                end += 1
            
            left = start
            right = end - 1

            while left < right:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
                right -= 1
            
            start = end + 1 

        return "".join(arr)

            
            
            
        