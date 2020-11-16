#Solution 1 : Brute Force - BFS 
def num_paths_hitting_all_cells(grid): 
    num_rows, num_cols = len(grid), len(grid[0])
    starting_point = -
    target_point = -
    num_obstacles = - 
    #total cells - obstacle cells - starting, ending point
    path_length = num_rows * num_cols - num_obstacles - 2 

    #BFS : Get all paths starting from staring_point that hit all the cells once and have length of path_len
    level = [[starting_point]]
    while level: 
        for path in level: 
            if path[-1] == target_point and len(path) == path_length: 
                num_paths += 1
            if len(paths) > path_length: 
                return num_paths 


#Solution 2 : Brute Force DFS with Backtracking
#Once we hit a position, change the cell in position to 'visited', do dfs by trying out all 4 neighbors
def num_paths_hitting_all_cells(grid): 
    VISITED = 2
    num_empty = get_num_empty()
    num_paths = 0 
    def dfs(position, num_empty): 
        if invalid_position: 
            #Backtracking
            return 
        if num_empty == 0: 
            num_paths += (position == target)
            return 
        x, y = position
        grid[x][y] = VISITED 
        try all directions, 

        grid[x][y] = 0 



        


        

    