#BEFORE HINT
#Solution 1 : Brute Force - for every connection check if it's critical 
#N servers, C connections => Time = O(C * N)

def critical_connections(N, connections): 
    def is_critical(connection): 
        graph.remove(connection)
        if can_reach_all_nodes(graph): 
            return True
        else: 
            return False
    critical_connections = []
    for connection in connections: 
        if is_critical(connection): 
            critical_connections.append(connection)
    return critical_connections


#Solution 2 : When is a connection not critical?
#When you can reach u, v with two paths. For an undirected graph, it means there is a loop. 
#So u - v connection is not critical if u and v lie on the same loop.
#Step 1. Detect all the loops in the graph 
#Union Find Method
#For every edge: connect edge. If it's already connected- cycle exists.
#Step 2. Return all the connections that do not lie on the loop
#Use union find algorithm.

#AFTER HINT 
#Skip Solution - involves tarzen algorithm

#In normal DFS, we just need to know weather we have visited the node or nah. 
#In this, we use rank for a node, which also tells the length of the cycle apart from wheather there is a cycle.
for child in graph[node]: 
    if child != node_parent: 
        if child in visited: 
            #found cycle 

        dfs(child)
    