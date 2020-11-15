def num_paths_hitting_all_cells(grid): 
    num_rows, num_cols = len(grid), len(grid[0])
    starting_point = -
    target_point = -
    num_obstacles = - 
    #total cells - obstacle cells - starting, ending point
    path_length = num_rows * num_cols - num_obstacles - 2 

    #BFS : Get all paths starting from staring_point that hit all the cells once and have length of path_len
    
