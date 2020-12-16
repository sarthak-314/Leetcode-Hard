### POST MORTEM
#Problem Pattern : Knapsack Problem
#Solution : Top Down Dynamic Programming
#Aleternate solution : You can also solve it with bottom up DP by iterating from 1 to target. Good solutoin
#I still got most of the solution. Cool. 

###


#Problem : Form largest Integer with digits - total cost of the int == target
#return int as string

#Problem Pattern 1 : Maximize something given an condition
#Problem Pattern 2 : Similar to Knapsack problem but greedy won't work as total cost is to be exactly equal.

#Possible Solutions : Dynamic Programming, Sorting, Greedy

#Solution 1 : Brute Force - DFS
# Make every possible integer with the final_cost == target, select the maximum of them 
#Time - Depends on Target

#Solution 2 : Dynamic Programming
#State = target - find the max integet you can make with rem_target

#CHECKS : Are all costs positive? 
#Assumption : Cost cannot be negative or zero

#Solution : Dynamic Programming
def form_largest_integers(costs, target): 

    #Returns the maximum integer we can make with rem_target
    def dp(rem_target): 
        if rem_target == 0: 
            return ''
        
        max_int = ''
        for c in range(0, 10): 
            #TODO: Add backtrakcing on rem_target
            res = str(c) + dp(rem_target - costs[c])

        return max_int

    
    return integer

#AFTER HINT 
#Yeah, I got the solution