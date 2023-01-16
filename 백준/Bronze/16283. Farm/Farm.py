a,b,n,w = map(int, input().split())

l = []

for i in range(1,n):
    if a*i+b*(n-i) == w:
        l.append([i,n-i])

if len(l) != 1:
    print(-1)

else:
    print('{} {}'.format(l[0][0], l[0][1]))