#Solution 1 : Brute Force
def is_sqareful(nums): 
    pass 

from itertools import permutations
def num_squareful_permutations(nums): 
    num_squareful_permuts = 0
    for permut in permutations(nums): 
        if is_sqareful(permut): 
            num_squareful_permuts += 1

    return num_squareful_permutations


#Solution 2: Squareful Pairs 
#Find all squareful pairs oin O(N ^ 2) time, 
#DFS with Backtracking
def num_squareful_pairs(nums):
    #Build graph
    graph = defaultdict(set)
    for i, n in enumerate(nums): 
        for j, n in enumerate(nums): 
            graph[i].add(j)
            graph[j].add(i)
    
    squareful_pairs = []
    num_squareful_pairs = 0
    def dfs(path): 
        #Basic Backtrakcing - you can do it.

