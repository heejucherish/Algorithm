import sys

input = sys.stdin.readline
num_list = []

def isRepeatless(num):
    repeat_list = [False] * 10
    while num / 10 != 0:
        if repeat_list[int(num % 10)] == True:
            return False
        else:
            repeat_list[int(num % 10)] = True
        num = int(num / 10)
    return True


i = 1
while len(num_list) < 1000000:
    if isRepeatless(i) == True:
        num_list.append(i)
    i += 1


while True:
    n = int(input())
    if n == 0:
        break
    print(num_list[n - 1])