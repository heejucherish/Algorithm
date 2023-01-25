import sys
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
t = int(input())
for i in range(t):  
    li=[]
    a=list(map(int,sys.stdin.readline().split()))
    for j in range(len(a)):  #a의 길이 만큼
        for k in range(len(a)):  #a의 길이 만큼
            if j>k and j!=k:  #본인보다 인덱스가 큰 애들만 짝짓기
                li.append(gcd(a[j],a[k]))  #리스트에 gcd 추가
            else:
                pass
    print(max(li))