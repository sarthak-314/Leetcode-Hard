#BEFORE LOOKING AT HINT

#Solution 1 : Brute Force - Find all possible submatrics - if sum is target: counter += 1
#Optimization - use some variation of prefix_sum to get sum of submatrix in constant time. 
#Time - (x1, y1) to (x2, y2) => O(N ^ 2) * O(N ^ 2) for all possible submatrics -
#Time Complexity somewhere between O(N ^ 4) to O (N ^ 6 )


#Simpler Version of Question - Number of subarrays that sum to target
#Sol : Use prefix sum to get O(N ^ 2) time complexity

#Solution 2 : 
# Optimization 1 : Use prefix sum for every row to get sum in O(N) time. 

#Solution 3 : 
#Binary Search? 


#AFTER LOOKING AT HINT

#1. The prefix sum intiution was right. Do one on the row and one on the column and you can query the sum of a 
#submatrix in constant time. That's epic. 

#Simpler Question = Number of subarrays that sum to K 
#You are gonna take the prefix sum. 
#My solution to this sucked. 
#Let's say the cur_prefix_sum is X, if we have seen X - k, we can make k. Linear Time baby.

#Solution :
#1. get prefix_sum_matrix, and a function to get sub matrix sum in constant time
#2. Forget matrix, think of it as an list. Take every possible combination of row_up, row_down and 
#think about the matrix[row_down : row_up] as a giant list. 
#3. Deploy prefix sum hash table method to get the result in linear time for that matrix



def num_submatrices_with_sum_target(matrix, target): 
    
    def get_prefix_sum_matrix(matrix): 

        return prefix_sum_matrix


    def submatrix_sum(top_left, bottm_right): 

        return submatrix_sum 

    num_cols = len(matrix[0])
    def get_num_subarrays_sum_target(row_top, row_bottom): 
        #Think of it as an array with length num_cols and each element is row_top - row_bottom
        nums = []
        for col in range(num_cols):
            element = prefix_sum_matrix[row_bottom][col] - prefix_sum_matrix[row_top][col]
            nums.append(element)

        #Now, it's a leetcode medium problem. All you have to do is to find the number of subarrays in nums
        #that sum to target. With prefix sum, you can find the answer in Linear Time. ay
        return num_subarrays_in_nums_that_sum_to_target


    res = 0
    num_rows = len(matrix)
    for row_top in range(num_rows): 
        for row_bottom in range(row_top, num_rows): 
            res += get_num_subarrays_sum_target(row_top, row_bottom)

#Time Complexity - O(N ^ 3)
#Space Complexity - O (N ^ 2) for prefix_matrix