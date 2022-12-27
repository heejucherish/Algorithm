import sys

input = sys.stdin.readline


def solution(num, base):
    while num:
        tmp = num%base
        if tmp >1:
            return 'NO'
        else:
            num //= base
    return 'YES'


n = int(input())

if n == 0 :
    print('NO')
else:
    print(solution(n,3))

