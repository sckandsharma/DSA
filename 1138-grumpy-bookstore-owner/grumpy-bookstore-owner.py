class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        n = len(customers)

        satisfied_customers = 0

        for i in range(0,n):
            if grumpy[i] == 0:
                satisfied_customers += customers[i] 
        
        additional_satisfied = 0
        max_additional_satisfied = 0
        
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
        
        max_additional_satisfied = additional_satisfied

        for i in range(minutes,n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            
            if grumpy[i-minutes] == 1:
                additional_satisfied -= customers[i-minutes]

            max_additional_satisfied = max(max_additional_satisfied,additional_satisfied)

        return max_additional_satisfied + satisfied_customers