n = int(input())

arr = list(map(int, input().split()))
# 오름차순 정렬
arr.sort()

x = int(input())
# s가 왼쪽 e가 오른쪽 
s = 0
e = n -1

cnt = 0

while s < e:
    if arr[s] + arr[e]  == x:
        cnt += 1
        s += 1
        e -= 1

    elif arr[s] +arr[e] <x:
        s += 1
    else:
        e -= 1

print(cnt)