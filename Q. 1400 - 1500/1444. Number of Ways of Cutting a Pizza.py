#### POST MORTEM
#Problem Pattern 1 : Find number of ways to do something on an condition
#Solution : DFS to get all the ways, DP to cache the subproblems

#Subproblem : Find the number of apples a slice of pizza contains in constant time..
#Solution : Solve with prefix sum. Replace containg apple with 1 and not with 0
#To find the number of apples in a matrix, use 2d DP matrix with prefix sum.

####


#BEFORE HINT

#Problem Pattern : Find total number of ways to do something given some condition

#Solution 1 : Brute Force - DFS - try every possible combination
#Time - O( 2 ^ (N + M) ) loose upper bound (pizza dimensions = N x M)

#Solution 2 : Dynamic Programming 
#Same as DFS, but cache the results 
#State = pizza_grid => return the num ways to cut the pizza

#Solution : Dynamic Programming
def num_ways_to_cut_pizza(pizza_grid, num_slices): 
    num_cuts = num_slices - 1

    apples = find_apples()


    #returns the number of ways to cut the grid
    #Possible Optimzation : Instead of passing the entire grid, only pass the row and col indices
    #This can save both space in recursion stack and time of finding apples in the pizza
    def dp(pizza_grid, rem_slices): 
        #Base Case - no apples
        if not rem_apples or not rem_slices: 
            return not rem_apples and not rem_slices 
    return num_ways

#AFTER HINT 1
#Instead of passing the entire grid, you can just pass the coords for upper left corner, 
#All the pizzas after cutting have the lower right point in them.
#You just had to visualize the cutting a few times, you woulda got it. 
#If you are not perfectly sure about the solution, try fkin visualization.

#Now, we can optimize the DP, by passing top left point and rem slices
def dp(x_left, y_top, rem_slices): 
    for i in range(x_left): 
        #Try cutting pizza and do DP
    for j in range(y_top): 
        #Try cutting pizza and do DP    

#AFTER HINT 2 
#You need only try those cuts, which gives the person the pizza. 
#I'm thinking just do it greedily. 
#Binary Search for the apple, or better use prefix sum of something to get in constant time.



