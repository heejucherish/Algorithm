import sys
input = sys.stdin.readline

n = int(input())

tops = list(map(int,input().split()))

#print(tops)

st = []


for i in range(n):
    while st and tops[st[-1]] < tops[i]:
        st.pop()

    st.append(i)
    #print(st[-1])
    if len(st) >1:
        print(st[-2]+1, end = ' ')
    else:
        print(0 , end = ' ')
