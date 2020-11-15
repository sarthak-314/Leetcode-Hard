#Alternate Question Framing : given nums, multiply each num by -1, 1 or 0 such that it sums to 0. 
#Find a combination that gives the largest sum of positive numbers

#Solution 1 : Brute Force - DFS
def build_tallest_tower_dfs(rods): 
    pole1, pole2 = [], []
    max_height = 0

    def dfs(i): 
        #Base Case 
        if sum(pole1) == sum(pole2): 
            height = sum(pole1)
            max_height = max(height, max_height)

        #End Case
        if i == len(rods): 
            return

        rod = rods[i]

        #Case 1 : rod goes to pole1
        pole1.append(rod)
        dfs(i + 1)
        pole1.pop()

        #Case 2 : rod goes to pole2
        pole2.append(rod)
        dfs(i + 1)
        pole2.pop()

        #Case 3 : rod goes in neither
        dfs(i + 1)

    return dfs(0)

#Time Complexity - O(3 ^ N)
#Space Complexity - O(N)

#Solution 2 : DFS with memo
#Fucking shit - just add memo - it was that easy to get optimial solution
from functools import lru_cache
def build_tallest_tower_dfs2(rods): 
    @lru_cache(None)
    def dfs(idx, diff): 
        if idx == len(rods): 
            return 0
        rod = rods[idx]
        #Intiution : I am at index - idx and I have to make up for the difference diff. 
        #I can take three cases, add the rod to shorter height and increase diff, dont add or add to longer
        add_to_long = dfs(idx + 1, diff + rod)
        add_to_short = dfs(idx + 1, abs(diff - rod))
        dont_add = dfs(idx + 1, diff)
        
        max_height = max(add_to_long, add_to_short, dont_add)
        return max_height
    return dfs(0, 0)


#Solution 3 : Solved as Knapsack problem
def tallest_billboard(rods): 
    #If we got a pair of poles (a, b) with a > b, then dp[a - b] = b
    dp = {0 : 0}
    for rod in rods: 
        for diff, height in dp.items(): 
            #Add to longer rod - we update it to max(height or prev value)
            dp[diff + rod] = max(dp.get(rod + diff, 0), height)
            #Add to shorter rod
            dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0), height + min(diff, rod))
    return dp[0]





