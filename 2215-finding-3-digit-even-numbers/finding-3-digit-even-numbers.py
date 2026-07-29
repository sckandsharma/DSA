class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:


        u  = []
        count = Counter(digits)

        for i in range(100,999,2):
            for k, v in Counter(map(int,str(i))).items():
                if count[k] < v:
                    break
            else:
                u.append(i)

        return sorted(u)
