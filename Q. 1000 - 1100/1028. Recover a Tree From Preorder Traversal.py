#Preorder = Left => Node => right
#traversal_string => level = '-'.count before num
def recover_from_preorder(traversal_string): 
    # ---3--12---67---234---45 => 3, 12, 67, 234, 45 => integers 3, 12, 67, 234, 45
    node_vals = [int(x) for x in traversal_string.split('-')]
    # ---3--12---67---234---45 => ---,  --, ---, ---, ---
    # to get levels, simply take the lengths of the dashes
    node_levels = [len(x) for x in traversal_string.split(lambda x : x.isdigit)]
    node_val_to_level = {val : level for val, level in zip(node_vals, node_levels)}
    level_to_nodes = defaultdict(list)
    for val, level in zip(node_vals, node_levels): 
        level.append(val)

    #Preorder = Left, Node, Right
    #To get the root, get the node with lowest level


    #Approach 1. Build the tree level by level 
    #For each level, we have a list of nodes from left to right order, 
    def build_tree(traversal_string, level): 
        if not traversal_string: 
            return None 
        root_val_idx = min level node in traversal_string
        root_val = -
        root = Node(root_val)
        root.left = build_tree(traversal_string[ : root_val_idx ])
        root.right = build_tree(traversal_string[root_val_idx + 1 : ])
        
    
    #Approach 2. Build the tree recursively
    
    return root 


