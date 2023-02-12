n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []

s1 = 0
s2 = 0
while s1 <n and s2 < m:
    if arr1[s1] < arr2[s2]:
        ans.append(arr1[s1])
        s1 += 1 
    else:
        ans.append(arr2[s2])
        s2 += 1

while s1 < n:
    ans.append(arr1[s1])
    s1 += 1

while s2 < m:
    ans.append(arr2[s2])
    s2 += 1

print(*ans)