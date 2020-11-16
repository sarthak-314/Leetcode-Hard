#Find Number of subarrays with K unique digits
#Solution 1 : Brute Force - Time - O(N ^ 2) -> get all subarrays, count num unique, Space - O(1)
#Solution 2 : Sliding Window? - Time - Linear ; Space - O(1)

#Solution : Sliding Window
def num_subarrays_with_k_unique(nums, k): 
    num_uniques = 0
    seen = set()
    l, r = 0, 0
    for r, n in enumerate(nums): 
        seen.add(set)
        while len(seen) == k: 
            num_subarrays += 1
            seen.remove(l)
            l += 1

    return num_subarrays 

