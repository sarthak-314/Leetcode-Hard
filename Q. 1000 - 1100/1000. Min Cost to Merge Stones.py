#Solution 1 : Brute Force - BFS 

#Solution 2 : Greedy?
#Always merge the stones with min cost
#Dosent' work here

#Solution 3 : Sliding Window?
#Nah. Doesen't work

#Solution 1 : Brute Force
def min_cost_to_merge_stones(stones, k): 
    #Base Case 
    if len(stones) <= k: 
        merge_all = sum(stones)
        return merge_all
    
    #We have len(stones) - k + 1 possible ways of merging stones
    #One way is to try every possible way
    min_cost = float('inf')
    for start_i in range(len(stones) - k + 1): 
        merged_stones = stones[:i] + sum(stones[i: i + k]) + stones[i + k : ]
        cost = sum(stones[i : i+k]) + min_cost_to_merge_stones(merged_stones)
        min_cost = min(min_cost, cost)

    return min_cost

#Solution 2 : Dynamic Programming / Divide and conquer
#Cost at the last step = sum(stones)
#Think of the last step, we have to place k - 1 dividers in the stones,
# Fucking Divide and Conquer! with DP. 
#DP(left, right) = min(DP(left, mid) + DP(mid, right) + sum(left : right))

def min_cost_to_merge(stones): 
    
    #Try to merge stones[left : right] as much as we can 
    #Returns the merged cost
    @lru_cache(None)
    def dp(left, right): 
        if right - left == k:
            #TODO: Optimize with prefix sum 
            return sum(stones[left : right])
        res =  min(dp(left, mid) + dp(mid, right) for mid in range(l, r, k - 1))
        perfect_merge
        if perfect_merge: 
            res += sum(stones[left : right])
        return res 
        
