###POST MORTEM
#I misread the question, you can only swap adjacent digits
#That makes 
#Observations: 
#1. We want the smaller digits as left as possible
#2. If I want to move some number to some left_pos, all digits to left are shifted by 1


###

#Problem Pattern : Minimize a value given some condition

#Approach 1 : Greedy - at each step try to minimize the number
#Time - O(K * lg N)

#Solution 1 : Brute Force - DFS
#Try every possible solution
#Time - O(N ^ K) but guarenteed to give the best solution

#Observation:
#1. The order of swap is not important. Can be compared to XOR operation.

#Solution : Do DFS and add some cache. Prolly not the best solution. Still better than DFS


#AFTER HINT: 
#The hint does not make any fking sense at all. Why is there a window. Why is it of size k.

