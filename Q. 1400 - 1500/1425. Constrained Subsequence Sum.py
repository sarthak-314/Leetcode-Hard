#### POST MORTEM


####


#BEFORE HINT

#Problem Pattern 1 : Subsequence - Try DP
#Problem Pattern 2 : Maximize something given an condition - definately try DP

#Subsequnce with max skip length = k

#Solution 0 : Very Brute Force - find all subsequences with j - i <= k
#Take the sum and find max
#Time - O(2 ^ N) loose upper bound


#Solution 1 : Dynamic Programming
#state - i
#state does not depend on the next elements. Bottom Up DP is possible
#Try iterative DP later to save space
#looks like a dp-right problem
#CHECKS : If all nums are negative return 0 or min?

#Maximum subsequence sum for nums[i:]
def dp(i): 
    #Base Case
    if i == N: 
        return 0

    #If current position = i : 
    #Case 1. Include i in the sequence
    include_i = max(dp(j) + nums[i] for j in range(i - k))
    #Case 2. Don't include i
    #TODO: Try optimizing so it don't use a loop
    exclude_i = max(dp(j) for j in range(i))

    return max(include_i, exclude_i)

    for j in reversed(range(i - k)): 
        return 

