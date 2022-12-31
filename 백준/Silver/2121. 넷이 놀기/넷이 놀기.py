import sys

input = sys.stdin.readline


def turn(p):
    global check_list
    lt = 0
    rt = len(check_list)-1
    while (lt <= rt):
        mid = (lt + rt)//2
        if check_list[mid] == p:
            return True

        elif check_list[mid] > p:
            rt = mid - 1

        else:
            lt = mid+1

    return False


N = int(input())
check_list = []

width, height = map(int, input().split())


for _ in range(N):
    x, y = map(int, input().split())
    check_list.append((x, y))

check_list.sort(key=lambda x: (x[0], x[1]))

answer = 0

for i in check_list:
    x, y = i[0], i[1]

    p1 = (x+width, y)
    p2 = (x, y+height)
    p3 = (x+width, y+height)

    if turn(p1) and turn(p2) and turn(p3):
        answer += 1


print(answer)
