# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        n = mountainArr.length()
        #finding the peak element first
        low = 0
        high = n - 1
        peak = 0

        while low < high:
            mid = low + (high-low)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                low = mid + 1
            else:
                high = mid

        peak = low


        #applying binary search on the increasing slope 

        low = 0
        high = peak
        while low <= high:
            mid = low + (high-low)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid+1 
            else:
                high = mid-1


        #applying binary search on the decreasing slope 

        low = peak
        high = n - 1

        while low <= high:
            mid = low + (high-low)//2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            
            elif val > target:
                low = mid + 1
            
            else:
                high = mid - 1 

        return -1 


        

        