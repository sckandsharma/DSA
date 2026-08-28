class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        #code here
        n = len(start)
        class Meeting:
            def __init__(self,start,finish,position):
                self.start = start
                self.finish = finish
                self.position = position
                
                
                
        meet = [Meeting(start[i],finish[i],i+1) for i in range(n)]
        
        meet.sort(key = lambda x:(x.finish , x.start))
        
        result = [1]
        last_time = meet[0].finish
        count = 1
        
        for i in range(1,n):
            if meet[i].start > last_time:
                count += 1
                result.append(meet[i].position)
                last_time = meet[i].finish
                
        return count
        
        