import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split()))for i in range(n)]
dp = [[-1 for i in range(3)] for j in range(1010)]

def recur(cur, prv):
    global ans
    if cur == n :
        return 0

    if dp[cur][prv] != -1:
        return dp[cur][prv] 
    ret = 1<<30
    for i in range(3):
        if i == prv:
            continue
        
        ret = min(ret,recur(cur+1, i )+ arr[cur][i])
    
    dp[cur][prv] = ret
    return ret



print(recur(0,-1))