#Solution 1 : Brute Force - loop from 1 to N, if num has repeated total += 1
#Time - O(N * lgN) => Linear to loop, lg n to check.
def nums_with_repeated_digits(N): 
    def has_repeated_digits(num): 
        return len(set(str(num))) != len(str(num))

    total = 0
    for i in range(N): 
        if has_repeated_digits(i): 
            total += 1 
    return total 

#Solution 2 : Iterative on num as array
#N = 3147
#Posssible answers => X, XX, XXX, 1XXX - 2XXX, 30XX to 31XX, 314X to 3147
from itertools import permutations
def nums_with_repeated_digits(N): 
    
    def n_digits_no_repeat(num_digits): 
        if num_digits == 1: 
            return 9 
        return 9 * len(permutations(range(9), num_digits - 1))
    
    total = 0 
    num_digits = len(str(N))
    for i in range(num_digits): 
        total += n_digits_no_repeat(i)
        start = 1 if not i else 0 
        for j in range(start, nums[i]): 
            if has_repeated(nums[:i]): 
                continue
            total  += 1
    return total 