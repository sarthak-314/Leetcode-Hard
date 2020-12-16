#Question Pattern : Knapsack Problem - for each column either keep the column or delete it
#Minimize the deleted columns on the given condition - all rows must be sorted

#Solution 1 : Brute Force - DFS -> iterate through the columns, either keep it or remove it
#N rows, M columns Time Complexity = O(2 ^ M * N) #Each column has 2 choices, -> Total of M columns
def delete_min_columns_to_make_sorted(matrix): 
    num_rows, num_cols = len(matrix), len(matrix[0])
    columns_deleted = []
    columns_kept = []
    def dfs(j): 
        #Currently at jth column    
        jth_col = list(zip(*matrix))[j] 
        cur_chars = []
        #Case 1. Keep jth column
        #We can only keep jth column if sorted condition satisfied
        #Get chars for all the rows 
        def can_add_j(j):
            if not columns_kept: 
                return True
            #Last column kept
            prev_col = columns_kept[-1]
            prev_chars = [string[prev_col] for string in matrix]
            cur_chars = [string[j] for string in matrix]
            for prev, cur in zip(prev_chars, cur_chars): 
                if ord(cur) < ord(prev): 
                    return False
            return True

        if can_add_j(j): 
            prev_chars = cur_chars
            dfs(j + 1)
        
        #Case 2. Delete jth column
        columns_deleted.append(j)
        dfs(j + 1)
        columns_deleted.pop(j)


#Solution 2 - Recursive Dynamic Programming
#Each column can either be added or not. 

#Problem Reframe : Instead of deleting columns, think about what columns to keep. 
#Find the max columns that you can keep while keeping every row sorted
#(Bad code)
def delete_min_columns_to_make_sorted_2(matrix): 
    #returns all the columns that can be kept
    def dp(i):
        #Base Case
        if i == 0: 
            return []
        columns_kept = dp(i - 1) + [i]
        strings = [''] * len(matrix)
        can_keep_column = True
        for col in columns_kept: 
            for i, string in enumerate(strings): 
                string += matrix[i][col]
                if not sorted(string) == string: 
                    can_keep_column = False 
        if can_keep_column: 
            return dp(i - 1) + [i]
        else: 
            return dp(i - 1)
        
    columns_deleted = dp(0)
    return columns_deleted 


#Solution 3 - Better DP
#Problem Reframe : Minimum numbers of columns kept to keep sorted
#Problem Pattern : left, right. Found the shit till left, now we try to add right. Solve by iterative DP
#(Good Code)
def delete_min_columns_to_make_sorted_3(strings): 
    #DP[i] = last column kept, number of columns kept
    dp = {0 : ([], 0)}
    columns = list(zip(*strings))
    num_cols = len(strings[0])
    for left in range(num_cols): 
        for right in range(left, num_cols):
            left_col, right_col = columns[left], columns[right]
            can_add_right_col = all(ord(string[right]) > ord(string[left]) for string in strings)
            if can_add_right_col: 
                dp[right] = max(dp[right], dp[left] + 1)
            


