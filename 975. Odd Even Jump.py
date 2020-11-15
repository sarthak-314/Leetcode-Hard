#Solution 1 : Brute Force - start from 0, simulate the jumps
def can_jump_to_end(nums): 
    can_jump = [False] * len(nums)
    #Start from jump = 1, odd numbered jump
    is_jump_even = False 
    for i, num in enumerate(nums): 
        j = get_j_idx(nums, i, is_jump_even)
        if is_jump_even: 
            j = min_idx(i)
        else: 
            j = max_idx(i)
        
        is_jump_even = not is_jump_even



    

    return can_jump