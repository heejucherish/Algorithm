a,b,c,p= map(int,input().split())

cnt = 0
for i in range(p//a+1):
    for j in range(p//b+1):
        for k in range(p//c+1):
            if a*i+ b*j+ c*k == p:
                cnt = 1

if cnt == 1:
    print(1)

else:
    print(0)