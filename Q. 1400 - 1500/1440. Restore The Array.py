####  POST MORTEM
#Easy Problem: Basic DP
# Problem Pattern : Count ways to make somrthing given an condition
# Solution : DFS / DP
# Solve with DP left and bottom up Dynamic Programming. 
# DP left solves [i : ] while DP right solves [ : i]
# If the solution is bi directional, use DP left because it can be made iterative. 
###

#BEFORE HINT

#Problem Pattern 1 : Count the number of ways to make something given an condition
#Solution 1 : Brute Force - DFS - try all possible combinations

#Solution 2 : Dynamic Programming - Same as DFS, but with caching
#State - DP-right problem, take i as state
#State is independent of the elements before it
#Can be solved with Bottom Up DP - do iterative DP to save recursion space


#Soluion : Dynamic Programming

def restore_array(printed_array, upper_limit): 
    #nums in array between 1 and upper_limit
    #Returns total number of ways to make the arrays from printed_array[i:]
    def dp(i):  
        #Base Case - built an array
        if i == len(printed_array): 
            return 1 
        res = 0
        for j in range(len(printed_array)): 
            number = printed_array[i : j]
            res += dp(j)

    return num_possible_arrays