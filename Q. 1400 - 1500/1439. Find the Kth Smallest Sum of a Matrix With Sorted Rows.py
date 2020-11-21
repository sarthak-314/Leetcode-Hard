#POST MORTEM 
#Problem Pattern 1 : Kth smallest in a matrix
#Solutions : Think about heap 

#Brute Force Solution 1 : My Brute Force 

#Better Brute Force Solution 2 : Iteratively combine the rows of the matrix and find the kth smallest
#The optimization over brute Force is that at every step, it only takes the k smallest solution, saving space and time
#Intiution : Think of it as DP over rows, DP-right, if you will. Combination of DP and DFS. 

#You can solve it with heap or with DP. I got the heap answer but could not come up with the DP-right.
#DP-right solution was good because DP[i] stores the k smallest sorted answers.

#BEFORE HINT
#Find kth smallest sum of a matrix with sorted rows

#Problem Pattern 1 : Find kth smallest in a sorted matrix
#Possible Solutions : Heap, Binary Search, Zig Zag, Brute Force
#Matrix - N x M

#Solution 1 : Brute Force - get sums of all the possible arrays - sort them - find kth element
#Time - O(M ^ N) to get all the possible arrays,  O(M) to get the sum and O(N lg N) to sort the elements
#Total Time Complexity ~ O(M ^ N)

#Possible Solution 2 : Heap?
#Start with pointers to the first elemets in all the rows of the matrix.
#Move the smallest element forward.
#Step 1. Make a diff list of lists

#Solution : Brute Force Iterative
def find_kth_smallest_sum(matrix): 
    num_rows, num_cols = len(matrix), len(matrix[0])
    pointers = [0] * num_cols 
    #TODO: Edge Case - matrix with one column
    heap = [row[1] - row[0] for row in matrix]
    for _ in range(k): 
        #ith array with p pointer
        #Possible Optimzation : Use Heap
        for i, p in pointers: 
            row = matrix[i]
            #Move the pointer with the smallest difference forward 
    
    return sum(matrix[i][x] for i, x in enumerate(pointers))


    return kth_smallest 

#Time Complexity - lg N for heap operations * k for linear scan
#Time - O(K) average time 
#Time - O(M ^ N * lg N) absolute worst time complexity
#TODO: Improve on worst time

#AFTER HINT: 
#Yaaas, I got the fking answer