#BEFORE LOOKING AT HINT

#Solution 1 : Very Brute Force - Counter on all possible substrings
#Time - O( N ^ 3 )

def longest_duplicate_substring(string): 
    seen = set()    
    duplicates = set()
    for l in range(len(string)): 
        for r in range(l, len(string)): 
            if substring in seen: 
                duplicates.add(substring)
            substring = string[l : r]
            seen.add(substring)
    
    return list(seen).sort(key=len)[0]

#Simpler Version => find most frequent char 
#Time - Linear, Space - Constant

#Approach 1. Maybe something like KMP algorithm? idk.

#Solution 2 : Reverse BFS with sliding window of fixed size. 

#Check all possible substrings of length N - 1 => N - 2 => N - 3, until you find the substring
#Returns 0 if no duplicate substring
def longest_duplicate_substring_2(string): 
    seen = set()
    N = len(string)
    for substring_len in reversed(range(N - 1)): 
        #substring = string[start_i : start_i + substring_len]
        #TODO: Edge Cases
        for start_i in range(N - substring_len): 
            substring = string[start_i : start_i + substring_len]
            if substring in seen: 
                return substring
            seen.add(substring)
    
# I don't think I can do better than reverse BFS 

#AFTER HINT
#For a substring length M, you can find wheather a duplicate substring of that length exists, in Linear Time + Linear Sapce
#Instead of M from range M to 0, fking Binary Search for the value for M.
#If a duplicate substring of length X exists, a duplicate substring of length 1, 2, 3 --- X - 1 also exists

#Solution 3 : Binary Search for the length of substring
def longest_duplicate_substring_3(string): 
    cur_substr_len = len(string)

    #Time - (N * M), where N = len(string) and M = len(substring)
    #Use KMP algorithm for Linear Time, 
    def get_duplicate_substrings_of_length(substr_len): 

        return duplicate_substrings

    l, r = 0, len(string)
    while r > l: 
        mid = (r + l) // 2 
        if get_duplicate_substrings_of_length(substr_len): 
            r = mid 
        else:
            l = mid 

    return r or l #TODO

#Time Complexity - O(N ^ 2 lg N) with regular pattern searching
#Optimized Time Compexity - O(N lg N) with better pattern searching algorith like KMP / Rabin Karp

#TLDR : 1. Use Binary Search
#2. You should know that there are pattern finding algos that work in Linear Time. Don't try to learn them.
#Don't try to implement KMP / Rabin Karp in interview .Even if interviewr asks to implement them, say no.



