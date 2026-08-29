class Solution:
    def findMin(self, n: int) -> int:
       # code here 
       
       total = 0
       
       total += n//10
       reminder = n % 10
       
       if reminder != 0:
           total += reminder // 5
           next_reminder = reminder % 5
           
           if next_reminder != 0:
               total += next_reminder // 2
           
               next_reminder = next_reminder % 2
               if next_reminder != 0:
                   total += 1
        
       return total
               
           