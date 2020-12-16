## POST MORTEM
#Some fancy algorithm. Skip the solutoin
##


#Solution 1 : Brute Force 
#O(K) for each query
#Simple iteration * k times


#Solution 2 : Caching
#Time Complexity might be reduced to lg K with binary search.
#Initialization Time Complexity - O(N * N)
#Query Time Complexity - O(1)

#Possible Solution 3 : Smart Caching
#

from functools import lru_cache
class TreeAncestor: 
    def __init__(self, parent): 
        self.parent = parent 

    @lru_cache(None)
    def get_kth_ancestor(self, node, k): 
        if k == 0: 
            return node 

        return self.get_kth_ancestor(self, parent[node], k - 1)
        
