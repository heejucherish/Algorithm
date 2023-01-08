
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    # 방문한곳 0으로 만들어주기
    board[x][y] = 0
    for i in range(4):
        xx = x+dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)


n = int(input())

board = [[0]*n for _ in range(n)]

for i in range(n):
    line = input()
    for j, b in enumerate(line):
        board[i][j] = int(b)


res = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            DFS(i, j)
            res.append(cnt)


print(len(res))
# sort 해줘야한다! 그래야 오름차순
res.sort()

for x in res:
    print(x)
