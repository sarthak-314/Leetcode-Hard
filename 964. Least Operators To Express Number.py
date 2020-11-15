#Solution 1 : Brute Force - BFS
def least_operators_to_make_target(num, target): 
    operators = '+-*/'
    num_operators = 0
    eval_strings = [str(num)]
    while True: 
        for eval_string in eval_strings: 
            for operator in operators: 
                new_eval_string = eval_string + operator + str(num)
                if eval(new_eval_string) == target: 
                    return num_operators
                eval_strings.append(new_eval_string)

        num_operators += 1

#Solution 2 - Recursive + Greedy 
#Alternate framing -> current state = num, target
#Similar to coin shange?
#The problem said, we don't got any brackets. But if we did had brackets, this won't work
#In this the state is target. We can aim for a new state, by modifying target. The state is independent of previous
#operators in whatever order used. We care bout only target

#Modified Question : You can use brackets
#Answer : You modify the number and the target. The state will consist of both the number and the target. 
#The number gets modified to 4 possible operations. Remember that set(/ or 0), math.isclose

def least_operators_to_make_target_2(num, target): 
    #Base Case
    if num == target: 
        return 0
    
    #Case 1. num < target
    # We move greedily, multiplying the number by iterself multiple times
    multiplied = num 
    times_multiplied = 0
    while multiplied < target: 
        multiplied *= num
        times_multiplied += 1
    if multiplied == target: 
        return times_multiplied

    #Similar to gas tank problem, we have two choices, one to go forward, other to go backward, and one to stay
    forward = least_operators_to_make_target_2(nums, target - multiplied) + times_multiplied
    backward = least_operators_to_make_target_2(nums, target - multiplied / num) + times_multiplied - 1
    return min(forward, backward) + 1
    


#Solution 3 - Answer to a modified question. You can use brackets 
def least_operators_to_make_target_3(cur, x, target): 
    if math.isclose(cur, target): 
        return 0
    next_possible_cur = {cur * x, x and cur / x, cur - x, cur }
    for next_num in next_possible_cur: 
        return 1 + least_operators_to_make_target_3(next_num, x, target)

    

