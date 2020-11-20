#BEFORE HINT 
#Solution 1 : Standard DFS with Backtracking
#Start from cell 1 and stop when every cell is painted.
#Time Complexity - Total 3 ^ (N * N) possible cases, but backtracking makes sure we don't visit all.
# Time - O(3 ^ (N*N)) loose upper bound. 

#Possible Solution 2 : Math / Dynamic Programming
#Answer is some function of N, DP could help find the function.
#DP[N] = func(DP[N - 1], DP[N - 2]) ??
#Starting with N = 1, res = 12
#For N = 2, res = DP(1) ^ 2 - some cases where colors overlap.
#  


#Possible Solution 3 : Divide and Conquer?


#AFTER HINT
#The DP intiution was right. But I didn't make any progress.
#Fuck. I thought we find DP(N) from DP(N - 1), DP(N - 2). We don't do DP on N, but on the cells. 
#Let's say I'm at some cell - i, j. We gotta color it.
#You have a grid of dimension N x 3. The time complexity is wrong. It's 3 ^ 3N.
#Think bout this - for a row, you got 12 possible color combinations. 
#When you go to next row, you have dp[row_idx][prev_col1][prev_col2][prev_col3]
#Instead of state of N, you have state of N, prev_col1, prev_col2, prev_col3
#Now DP is easy. You can even save on some space with Bottom Up iterative DP 

def num_ways_to_paint(N): 
    #If I am at row with row_idx, it returns the possible ways of coloring the next N - row_idx rows.
    def dp(row_idx, prev_col_1, prev_col_2, prev_col_3): 
        if row_idx == N: 
            return 0 
        res = 0
        for p1, p2, p3 in all_possible_next_states:  
            res += dp(row_idx, p1, p2, p3)

        return res 


#You can now solve in Linear Time. Now that's a big fking improvement

#AFTER SOLUTION
#Wait, you can do even better. The DP(N) solution works. needs some math though.
#There are only two cases for each row - 123, 121
#Take both cases and make a DP equation
#You can do it with iterative DP

#Chad Solution : 
all_diff, two_same = 6, 6 
for i in range(2, N): 
    all_diff = 2 * all_diff + 3 * two_same 
    two_same = 3 * all_diff + 2 * all_same 

#This reminds me of that problem where you have to find all the numbers with zero / one binay codes.

#God Solution : 
#Something using adjacency matrix and numpy. idk maybe i'll try to understand it later when I have time. No sane interview will expect this solution/.

