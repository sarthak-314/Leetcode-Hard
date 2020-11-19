#BEFORE HINT
#Solution 1 : Very Brute Force - Try every possible pair of i, j - check if it's strictly increasing
def make_nums_strictly_increasing(nums1, num2): 
    def is_strictly_increasing(nums): 
        return nums == sorted(nums)
    
    for i in range(len(nums1)): 
        for j in range(len(nums2)): 
            nums1[i] = nums2[j]
            if is_strictly_increasing(nums1): 
                return nums
    
#Time Complexity = O(N ^ 3 * lg N), Space = O(N)

#Solution 2 : Greedy Swap with Binary Search 
#For every position, swap it with a number just greater than prev 
#Sort second nums
#Still Brute Force but Time - O(N * lg N)

#Solution 3 : Some Linear Time Algorithm
#Sort nums2. Don't know if it exists 


#AFTER HINT
#The sorting intiution was right. I don't know how it uses Dynamic Prgramming
#I can take a pointer to reduce the search space after every search. 
#iterative solution should work fine. Why do i need dynamic programming.
#You have to minimize the operations you fking moron. 

#TODO: Longest Increasing Subsequence