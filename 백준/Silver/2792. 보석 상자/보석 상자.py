import sys
input = sys.stdin.readline

N, M = map(int, input().split())
color_list = []
for _ in range(M):
    color_list.append(int(input()))

start = 1
end = max(color_list)

while start <= end:
    mid = (start+end) // 2
    total = 0
    for color in color_list:
        if color % mid == 0:
            total += color//mid
        else:
            total += (color//mid) + 1
    # total이 더 크다는 것은
    # N명보다 더 많은 사람이 보석을 가져간 것
    # 그렇기 때문에 더 적게 가져가도록 하기위해 left를 증가시켜야함
    # 한 명이 가져가는 보석의 수를 늘림
    if total > N:
        start = mid + 1

    else:
        end = mid - 1

print(start)