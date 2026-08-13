class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True 

            seen.add(num)

        return  False


    #similarly we can do for a stirng 
        
        # seen = set()

        # for ch in s:
        #     if ch in seen:
        #         return True

        #     seen.add(ch)

        # return False
        
        