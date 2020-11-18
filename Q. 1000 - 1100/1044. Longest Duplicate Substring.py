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

#Solution 2 : Reverse BFS
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
    


