def print_grid(matrix): 
	s = [[str(e) for e in row] for row in matrix]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print('\n'.join(table))


N, num_checkpoints = [int(x) for x in input().split()]
checkpoints = []
checkpoints_cells = set()
for idx in range(num_checkpoints): 
    x, y, l, r = [int(x) for x in input().split()]
    checkpoints.append((x - 1, y - 1, l, r, idx))
    checkpoints_cells.add((x - 1, y - 1))

    
pairs = []
for i, (x, y, l, r, idx1) in enumerate(checkpoints): 
    for x2, y2, l2, r2, idx2 in checkpoints[i + 1:]: 
        dist = abs(x - x2) + abs(y - y2)
        if dist < max(l, l2): 
            continue
        min_len, max_len = dist, min(r, r2)
        pairs.append([(x, y), (x2, y2), (min_len, max_len), (idx1, idx2)])

visited = set()




def get_connecting_paths(pair): 
    (x, y), (x2, y2), (min_len, max_len), (idx1, idx2) = pair
    cur_len = 0 
    #List of all the paths 
    level = [[(x, y)]]
    while cur_len <= max_len: 
        if min_len <= cur_len <= max_len:  
            for path in level:
                if not path: 
                    continue
                if path[-1] == (x2, y2):
                    for node in path[:-1]: 
                        if node in checkpoints_cells: 
                            continue
                    # print('PATHSTA : ', path)
                    yield path
            
        next_level = []
        for path in level: 
            x_last, y_last = path[-1]
            directions = [-1, 0], [0, -1], [1, 0], [0, 1]
            for dx, dy in directions: 
                xx, yy = x_last + dx, y_last + dy
                if (xx, yy) in visited or xx < 0 or xx > N or yy < 0 or yy > N: 
                    continue
                next_level.append(path + [(xx, yy)])
                
        level = next_level
        cur_len += 1

grid = [[False] * (N + 1)] * (N + 1)

print_grid(grid)
	
checkpoints_visited = set()
def dfs(i): 
	#We reached the end
	if i == len(pairs): 
		return 0
	
	pair = pairs[i]
	(x, y), (x2, y2), (min_len, max_len), (idx1, idx2) = pair
	if (x, y) in checkpoints_visited or (x2, y2) in checkpoints_visited: 
		return dfs(i + 1)

    checkpoints_visited.add((x, y))
    checkpoints_visited.add((x2, y2))
	print('PAIR : ', pair)
	
	max_res = dfs(i + 1)
	for path in get_connecting_paths(pair): 
		#If any of the cell in visited, then skip the path 
		if any(cell in visited for cell in path): 
			continue
		
		print('BEFORE TRAVELLING THE PATH')
		print_grid(grid)
			
		#Travel the path 
		for cell in path: 
			x, y = cell
			grid[x][y] = True
		
		print('PATH : ', path)
		print('AFTER : ')
		print_grid(grid)
		
		res = 1 + dfs(i + 1)
		max_res = max(max_res, res)
		
		#Reverse the path 
		for cell in path: 
			x, y = cell
			grid[x][y] = False 
			
		print_grid(grid)
			
		
		
		
    #Reverse the path 
    checkpoints_visited.remove((x, y))
    checkpoints_visited.remove((x2, y2))
    return max_res
	
	
max_pairs = dfs(0)
print(max_pairs)
		
		
		
	
	