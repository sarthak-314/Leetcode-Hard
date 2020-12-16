#### POST MORTEM
#Problem Pattern 1 : Question that looks like math but is probably DP
#state = i, k, cur_max
#Problem Pattern 1.1 : State is independent of what's ahead. Bottom Up DP is possible. 
# Try iterative DP to save space
#Optimization 1 : Use 2D lists instead of tuples to save space
#Optimization 2 : Initializa the array for cleaner code

#Problem Pattern 2 : Count the number of ways to build something given condition

#Solution 1 : Very Brute Force - make all possible arrays and see if they satisfy the condition
#Time - O(M ^ N) to build all arrays and O(N) to check the condition

#Solution 2.1 : Recurive DP
def dp(i, k, cur_max): 
    #Backtracking 
    if not k: 
        return 0
    if i == N: 
        return k == 0
    res = 0
    for next_num in range(1, M + 1): 
        #Case 1. new cur_max
        res += dp(i + 1, k, cur_max)
        #Case 2. Old cur_max
        res += dp(i + 1, k - 1, next_num)
    return res
#Solution 2 : Iterative Bottom Up DP
def build_array_with_K_comparisions(N, K, M): 
    #Initalize with 0 because the tree branches that don't hit the point get a score of 0.
    dp = [[[0] * N] * K] * M
    #Initializa DP, i == N, return 1
    for j, k in itertools.product(range(M), range(K)): 
        if k == 0: 
            dp[1][j][0] = 1
        dp[1][j][k] = 0



#PYTHON TIPS: 
for i, j, k in itertools.product(range(M), range(N), range(K))
#use for triple for loops - especially in initializing bottom up DP

####


#You have N, M and K. Looks like a mathematical problem, DP is the way to go.
#As I go forward with i, the N will change
#At the current position i, the state is dependent on - i, k and the cur_max of the prevoius numbers chosen




#BEFORE HINT
#len(arr) = N, arr[i] bet 1 - M, search cost = K.
#array with N numbers that lie between 1 and M
#condition : length of strictly increasing subsequence in array = K
#TODO: Check for duplicates

#Solution 1 : Very Brute Force - make every possible array and see if it satisfies condition
#Time - O(M ^ N) to make every array * O(N) to find strictly increasing subsequece starting from 0

#Solution 2 : Dynamic Programming 
#vars - N, M, K 
#DP(i, K, cur_max) 
#Case 2. the maximum changes - we add a number bigger than all prev numbers
#Case 1. The max remains the same - added num is smaller than cur_max

def num_arrays_K_comparisions(N, M, K): 

    def dp(i, k , cur_max): 
        #Backtracking
        if k < 0: 
            return 0
        #Found an valid array
        if i == N: 
            return 1 
        res = 0 
        for next_num in range(1, M + 1): 
            #Case 1
            if next_num <= cur_max: 
                res += 1 + dp(i + 1, k, cur_max)
            else: 
                if not (k-1): 
                    continue
                res += 1 + dp(i + 1, k - 1, next_num)


#AFTER HINT
#Same. I got the answer

#AFTER SOLUTION
