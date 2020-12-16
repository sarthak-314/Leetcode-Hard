#POST MORTEM - Very Standard DP - medium question at best.


#Given : Garden with cherries, Goal : collect max cherries
#start1 = top left, start2 = top rigth
#Move : next row, 3 neighbors

#Simpler Version of Question : 1 robot cherry picker
#Solution : Dynamic Programming 
#DP State = (position) Time - O(M * N)

#Solution 1 :  Dynamic Programming
#Store the positions of both the robots and get the answer 
#Approach 1 : Bottom Up DP

#Solution : Bottom Up Dynamic Programming
#TODO: Make it iterative DP
#Possible Optimzation : Use symmetric version of subproblems

def cherry_pickup(garden): 
    robot_1 = (0, 0)
    robot_2 = (0, len(garden[0]))
    def dp()

