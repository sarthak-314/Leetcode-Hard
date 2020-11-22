### POST MORTEM
#Got the DP Solution, though took some time.
#Every hard problem on Leetcode is fking DP

###


#Problem : Allocate Mailboxes to minimize distace
#Return : min distance

#Problem Pattern 1 : Minimize a value given an condition
#Possible Solution : DFS / DP 

#Possible Optimal Solution : Try to solve it greedily
#GREEDY : 


#Brute Force Solution : Try every possible Value of mailboxes
#Each mailbox can be paired with multiple houses.
#Brute Force method would be try all the possible pairings

#Dynamic Progrmaming Solution : Try using DP to cache the results.
#DP State = i, remaining_num_mailboxes
#Most Optimal DP Approach : Try iterative bottom up DP for most optimal DP complexities

#Possible Solution 3 : Divide and solve - divide the houses into areas.
#Each area has it's own mailbox. We can greedily find the best mailbox position for each area
#Use pointers to divide into areas
#Time Complexity - O( N C K ) to try out all possible areas.
# Try DP to optimize complexity 
#Try bottom up DP for even more optimization

#ROUGH DRAFT
for i in range(len(houses)): 
    for k in range(num_mailboxes): 
        #Base Case - more / equal mailboxes than houses
        if k <= i: 
            dp[i][k] = 0 
            continue
        dp[i][k] = float('inf')
        #Possible Optimization : Replace the loop with constant time computation
        for i_prev in range(i): 
            dp[i][k] = find_min_distance(i_prev, i) + dp[i_prev][k - 1]

#Time Complexity = O(N * K * N)
#Space Complexity = O(N * K)

#Solution : Dynamic Programming + Greedy 
#Greedy : When allocating malboxes, position it at a house. It's at least as good as positioning it between houses.
#Dynamic Programing : Given, i and rem_mailboxes, return the min distance we can have with houses[i:] and rem_mailboxes.

#Still missing somthing, this does not look good.

#Possible Solution : Divide and Conquer
#



def allocate_mailboxes(houses, num_mailboxes): 


    return min_distance

