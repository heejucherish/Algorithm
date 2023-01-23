n = int(input())
num = list(map(int, input().split()))
result = 0

for i in num:

    if i == 1:
        continue
    cnt = 0
    for j in  range(2, i+1):
        if i % j == 0:
            cnt +=1
        
    if cnt == 1:
        result +=1

print(result)
        