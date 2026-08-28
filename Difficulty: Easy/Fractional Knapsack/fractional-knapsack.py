class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        
        
        arr = []
        
        for i in range(len(val)):
            arr.append((val[i],wt[i]))
            
        arr.sort(key = lambda x: x[0]/x[1],reverse = True)
        
        final_value = 0
        
        for value , weight in arr:
            if weight <= capacity:
                capacity -= weight
                final_value += value
            
            else:
                
                fractional_cost = (value / weight) * capacity
                final_value += fractional_cost
                break
            
        return round(final_value,6)
            