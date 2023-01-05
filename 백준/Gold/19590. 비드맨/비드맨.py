import sys

input = sys.stdin.readline


def check(num_list):
    max_num = num_list.pop()

    if max_num > sum(num_list):
        max_num = max_num - sum(num_list)
        return max_num

    else:
        if (max_num+sum(num_list)) % 2 == 1:
            return 1
        else:
            return 0


n = int(input())

num_list = []

if n == 1:
    print(int(input()))

else:
    for _ in range(n):
        num_list.append(int(input()))

    num_list.sort()

    print(check(num_list))
