#POST MORTEM
#Question very similar to Candy Game on Codechef. 
#Problem Pattern 1 : Two Player DP 
#Problem Pattern 2 : DP[i] is independent of i-, only depends on next k results

#Solution 1 : Regular Top Down DP - Linear Time and Linear Space
#Solution 2 : Reverse the parameter to make a DP right problem.
#Make this bottom up and solve iteratively.
#One loop because top down in linear space. Solve in Linear Time and constant Space

#BEFORE HINT
#Think about the last turn. When less than 3 stones remaining, best to take them all
#Dynamic Programming should be helpful. We just need to tell who won.
#If you are at position i, what's the most optimal gameplay. Looks like a DP(right) problem.
#If I'm at i, I coulda switched at i - 1, i - 2, i - 3.

#Assumption : Each player wants to win the game, so the primary objective is to get maximum stone values and seconda
#secondary objective is to reduce the opponent's stone values. 
#Approach 1 : Each player plays greedily, taking 3 stones every time
#Approach 2 : Each player plays optimially. 
def stone_game(stone_values): 

    #TODO: Edge Cases / One offs
    def dp(i): 
        #Base Case - less than 3 stones remaining
        #Move - pocket all of the stones, give your opponent 0
        if i >= len(stone_values) - 3: 
            return sum(stone_values[i:]), 0 
        
        #Case : More than 3 stones remaining.
        #Possible Moves : Take 1 stone, take 2 stones, take 3 stones
        
        #Play with the objectives in mind.
    
    alice_score, bob_score = dp(0)
    return result

#Top down dp make more sense. When you at position i, that's the start_i, not right_i

#AFTER HINT 
#My solution was correct, but there could be one more optimization. 
#We know in the end the total score for bob and alice is sum(stone_values). Don't need to take two variables.
#Reminds me of the burner problem on codechef. 
#The rest of the solution's the same


#AFTER SOLUTION


#lee215 did it with bottom up constant space.
#If I'm at position i, I just need the result for i + 1, i + 2 and i + 3. 
#Won't work with Top Down, but if you do botton up, you can get the space comlexity down from Linear to constant.
#When you are at i the only thing that matters is what's after i, i - 1, i - 2, i - 3 results are useless.
#So you have to iterate through reversed(stones). This way you have the result for i + 1, i + 2, i + 3. 
#Think about this - when you iterate in reverse order, this becomes a DP right problem. 
#You know how to convert DP right into iterative. It's linear time, so only one loop should do. 
#And you require only the prev 3 results, so a list of size 3 should be good for constant space.












