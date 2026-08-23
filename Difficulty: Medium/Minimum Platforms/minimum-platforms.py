class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        # code here
        
        arr.sort()
        dep.sort()
        n = len(arr)
        
        count = 1
        ans = 1
        
        i = 1
        j = 0
        
        while i<n and j<n:
            if arr[i] <= dep[j]:
                count += 1
                i += 1
                
            else:
                count -= 1
                j += 1
                
            ans = max(count,ans)
            
        return ans
                
            
        