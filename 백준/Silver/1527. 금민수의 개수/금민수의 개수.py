from itertools import product

def solution():
    a, b = map(int, input().split())

    min = len(str(a))
    max = len(str(b))

    factor = ["4", "7"]

    res = []
    for i in range(min, max + 1) :
        sub = list(map(lambda x : int(''.join(x)), product(factor, repeat = i)))
        
        for s in sub :
            res.append(s)

    count = 0
    for r in res : 
        if r in range(a, b+1) :
            count += 1
        
        if r > b+1 :
            break
    
    print(count)
        
solution()