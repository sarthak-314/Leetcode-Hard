boi = set()

def dfs(i):
    if i == 10: 
        return 0 
    if i // 2 in boi: 
        return 3
    max_res = 0
    boi.add((i))

    res = 1 + dfs(i + 1)
    max_res = max(res, max_res)
    print('BIO : ', boi)

    boi.remove((i))
    return max_res

ay = dfs(0)
print(ay)
