#TODO: Revisit the following questions with similar pattern: 
#1. Longest Common Subsequence
#2. Longest Common Palindromic Subsequence
#3. Shortest Common Supersequence
#4. Uncrossed Lines

#### POST MORTEM
#If you focus on the subsequcnce part, you can come up with the DP solutoin. Not that hard.
#Now, think about bottom up programming - if you solved the question - that is maxium dot product 
#You already loop through i and j - doing it again is stupid and gets the time comppl
#for [:i] and [:j], you only have two cases, take i and j or don't
#There is no difference problem - the DP stores the max dot product. Period. No difference and shit.
#You choose the current product, not the previous product
#Apart from considering i - 1 and j - 1, you also have to consider i - 1, j  and i, j - 1 and i - 1, j -1 
#Think about the DP matrix
#You already have the answer for i - 1 with j. In just the prev iteration, you also have the answer for i, j - 1
#Think about it- similar to longest common subsequnce
#I think I got it. You can either take i, j or not take i, j for dp[i - 1, j - 1] 
#For DP[i - 1, j ] and DP[i, j - 1], you are allowing for i and j be taken. If it were not, you get i - 1, j -1



#Pattern : Bottom DP with Greedy 
for i in range(len(nums1)): 
    for j in range(len(nums2)): 
        if not i or not j: 
            dp[i][j]  = 0
        #Find the DP[i][j]
        dp[i][j] = max()
        #Case 1. Skip 

        #Case 2. Take the product

####

#Problem : Given 2 arrays, maximize the dot product of subsequences

#Problem Pattern 1 : Subsequences - try DP
#Problem Pattern 2 : Maximize a value given some conditions - definatley try DP

#Solution 0 : Very Brute Force - find dot products of all the subsequences, maximize sum
#Time - O(2 ^ N * 2 ^ N) loose upper bound

#Solution 1 : Dynamic Programming
#state - i, j - pointers for the two subsequences
#DP for state i, j is independent of previous elements
#We can take nums[i:], nums[j:]
#Problem should be solvable with bottom up DP


#Possible Solution 2 : Greedy Approach - might not work

#Solution 1 : Bottom up DP

#Step 2. Find Time and Space complexity
#Step 2. Clean and optimize code 
#ROUGH DRAFT SOLUTION
def max_dot_product_subsequences(nums1, nums2): 

    #Returns max dot product for nums1[i:] and nums[j:]
    def dp(i, j): 
        #Base case 
        if i == end or j == end: 
            return 0
        res = 0
        #TODO: Optimize this
        for i_next in range(i, len(nums1)): 
            for j_next in range(j, len(nums2)): 
                cur_res = in * jn + dp

        return res

    return max_dot_product 

#Current Time Complexity - O(N ^ 4)
#Current Space Complexity - O(N ^ 2) cache the result 
#TODO: Make the solution iterative bottom up DP after solving recursive

#Solution (Optimal) : Iterative DP
for i, j in itertools.product(range(len(nums1)), range(len(nums2))): 
    dp[i][j] = find it 
    for i_prev, j_prev in itertools.product(range(i), range(j)): 
        dp[i][j] = max()



