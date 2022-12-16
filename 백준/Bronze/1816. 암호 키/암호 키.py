import sys 

import math

input = sys.stdin.readline
n = int(input())
arr = [True for _ in range(1000000+1)]

for i in range(2, int(math.sqrt(1000000)) + 1):
    if arr[i] == True:
        j=2
        while i * j <= 1000000:
            arr[i*j] = False
            j += 1


for _ in range(n):
    number = int(input())
    result = "YES"

    for i in range(1000000+1):
        if i > 1:
            if arr[i] == True:
                if number%i == 0:
                    result = "NO"
                    break

    print(result)
            
