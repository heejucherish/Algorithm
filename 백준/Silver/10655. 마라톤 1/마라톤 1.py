import sys

check_point = int(sys.stdin.readline())
point_list = []
total_distance = 0
min_distance = 0

for i in range(check_point):
    point_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(point_list)):
    total_distance += abs(point_list[i][0] - point_list[i-1][0]) + abs(point_list[i][1] - point_list[i-1][1])

for i in range(1, (len(point_list)-1)):
    left_distance = abs(point_list[i][0] - point_list[i-1][0]) + abs(point_list[i][1] - point_list[i-1][1])
    right_distance = abs(point_list[i+1][0] - point_list[i][0]) + abs(point_list[i+1][1] - point_list[i][1])
    next_distance = abs(point_list[i+1][0] - point_list[i-1][0]) + abs(point_list[i+1][1] - point_list[i-1][1])
    skip_distance = left_distance + right_distance - next_distance
    min_distance = max(skip_distance, min_distance)
    
print(total_distance-min_distance)