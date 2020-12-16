#Solution 1 : Brute Force - BFS 
#Time - O(N ^ N) upper limit
def min_flips_to_all_ones(string, k): 
    level = [string]
    num_flips = 0
    while level: 
        next_level = []
        for s in level: 
            if s == '1' * len(s): 
                return num_flips
            for i in range(len(s) - k):
                next_s = flip(s, i)
                next_level.append(next_s)
            
        level = next_level
        num_flips += 1 


#Soluion 2 : Greedy 
#Linear Search -> whenever we encounter 0 => flip the next k digits. 
#1. Order of flip does not matter
#2. So we start from left to right
def min_flips_2(string, k): 
    is_flipped = [False] * len(string)
    for i, char in enumerate(string):
        need_to_flip = int(char) and is_flipped[i] == False 
        if need_to_flip: 
            is_flipped[i : i + k] = [not x for x in is_flipped[i : i + k]]
    
    return num_flips
    

#Solution 3 : Greedy but Linear Time 
def min_flips_3(string, k): 
    cur_flips, total_flips = 0, 0
    for i, char in enumerate(string): 
        #In the window string[i - k : i]
        #Update cur_flips - kind of like that nums questoin
        window_start = nums[i - k]
        if window_start > 1: 
            string[i - k] -= 2 
            cur_flips -= 1 
        #We flip if ->
        #Case 1. cur_flips is even and char is 0
        do_flip = int(char) or cur_flips % 2
        if do_flip: 
            cur_flips += 1 
            string[i] += 2 
            total_flips += 1 

        #Case 2. cur_flips is odd and char is 1 

