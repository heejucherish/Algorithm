n=int(input())
stats=list(map(int,input().split()))

res = 0
start, end = 0, n - 1
while start < end:
    
    res = max((end - start - 1) * min(stats[start], stats[end]), res)

    if stats[start] < stats[end]:
        start += 1
    else:
        end -= 1

print(res)