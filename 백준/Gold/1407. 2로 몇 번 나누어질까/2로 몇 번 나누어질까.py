a,b= map(int, input().split())

def func(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num % 2 == 0:
        return num //2 + 2*func(num//2)
    elif num % 2 == 1:
        return num //2 +2*func(num//2)+1

print(func(b) - func(a-1))