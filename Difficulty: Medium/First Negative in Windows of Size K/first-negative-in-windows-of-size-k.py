class Solution:
    def firstNegInt(self, arr, k): 
        
        FNI = 0
        ans = []
        
        for i in range(k-1,len(arr)):
            
            while FNI < i and (FNI <= i-k or arr[FNI] >= 0):
                FNI += 1
                
            if arr[FNI] < 0 and FNI <= i:
                ans.append(arr[FNI])
            else:
                ans.append(0)
                
        return ans
        
          
