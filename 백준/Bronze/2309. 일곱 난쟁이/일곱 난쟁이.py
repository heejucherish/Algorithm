n = 9
# 오름차순 정렬 
arr = [int(input()) for _ in range(n)] 

arr.sort()

s1 = 0 
s2 = n-1

#난쟁이가 아닌 애들을 찾자!
find = sum(arr) - 100
find_result = []

while s1 < s2:
    if find > arr[s1] + arr[s2]:
        s1 +=1
        
    elif find < arr[s1] + arr[s2]:
        s2 -=1
        
    else:
        find_result.append(arr[s1])
        find_result.append(arr[s2])
        break
        
for i in range(n):
    if arr[i] not in find_result:
        print(arr[i])
        