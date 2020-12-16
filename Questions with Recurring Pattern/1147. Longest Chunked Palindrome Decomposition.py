#BEFORE HINT

#Solution 1 : Brute Force - Split the first half of the string into every possible chunk. Check if it's a palindrome

#The answer lies between 1 and N.
#Solution 2 : Optimized Brute Force
#If we can split into K chunks, we can also split into K + 1, K + 2, K + 3 -- N chunks. 
#Binary Search for the value of res.
#Does Not Fucking Work - works on longest duplicate substring, not here. 

#Solution 3 : Dyanamic Programming
def longest_chunked_decomposition(string): 

    def dp(i): 
        max_res = 0
        for j in range(i + 1, len(string)): 
            #Try to make string[i : j] a chunk
            if can_be_chunked(i, j): 
                res = 1 + dp(j)
        
        return max_res

    return max_num_chunks
 
#Time Complexity is O(N ^ 2) - Epic. 

#For substrings, Dyanmic Programming and sliding window works for most cases. 
