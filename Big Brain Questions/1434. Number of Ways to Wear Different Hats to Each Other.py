####### POST MORTEM

#Not exactly a hard question, but it mixes different questions, so it prolly belongs here.

#SOLUTION 1: ASSIGN PEOPLE TO HATS 

#Brute Force Solution : DFS - Try every possible move. Obvious solution ; easy to come up with.

#Problem Pattern 1 : 0-1 Knapsack like Problem
#If you look more closely, you can tell it resembles knapsack. You can come up with DP once you realiza that.
#The DP state will be (hats_remaining, person_i)
#Knapsack usually solved by top down DP, you take the item or not take it. Basically DFS but with caching.

#Problem Pattern 2 : Count the total number of ways 
#Imagine as paths branching out from i = 0. Most of the paths are terminated early and get zero points. Some of them 
#complete and get one point. We need the total number of paths from i = 0 to i = n, so we assign the path only once
#it's complete. And we recurse. Think of it as tree with root at i = 0 and multiple branches at i = n. 
#Each node is sum(children). We find the value of root by recursion. 
#if i == n : return 1 ans = 0 ans += dp(i + 1, hats_rem)

#SOLUTION 2 : ASSIGN HATS TO PEOPLE
#Cool thing to note is num_people < 10 but num_hats = 40. 
#Make hat_to_people = defaultdict(list)
#Basically the same solution afterwards

#######



#BEFORE HINT
#Problem Pattern : Similar to Knapsack Problem
#Knapsack but instead of maximizing a value, we have to count the total possible combiantions

#Solution 1 : Brute Force - DFS with backtracking
#Try every possible combinatiom
#Time - O(40 ^ N) loose upper bound


#AFTER HINT 
#why did you look at hint You could have done it man.
#Solution 2 : Dynamic Programming
#DP state depends on remaining_hats and cur_person
#Time - O(40! * N) 

#ROUGH WORK - Recursive DP.
#state is person i and hat set
#if i'm at person i with hats_rem, how many possible ways are there?
def dp(i, hats_rem): 
    if i == all: 
        return 0 
    if not hats_rem: 
        return 0 
    res = 0
    for hat in hats: 
        #Basically DFS, but I cache the result.

        res += dp(i + 1, hats_rem.remove(hat))
    return res 


#Solution 3 : Iterative Dynamic Programming for O(40) space
#Time - Same as Sol2, but better space complexity
def num_ways_to_wear_hats(hat_preferances): 
    TOTAL_HATS = 40
    total_ways = 0 
    #Possible but unnecessary optimization - use bitmask, still constant space. 
    hats_remaining = set(range(1, TOTAL_HATS + 1)) 
    #State : (i, hats_rem) - currently at ith person with hats_rem : set of hats remaining
    #TODO: Optimize for space
    dp = {}
    #Possible but unnecessary optimization - use bitmask instead of set
    visited = set()
    for i, hat_pre in hat_preferances: 
        for hat_rem in hat_rem_pre: 
             for hat in hats: 
                 if hat not in hats_remaining: 
                     continue
                #Choose hat and next dp 
                else: 
                    updte hats_rem 
    return total_ways


