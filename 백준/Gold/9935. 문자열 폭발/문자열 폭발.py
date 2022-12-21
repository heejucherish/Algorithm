st = []
# 문장
s = input()
# 없애야 할 단어 
p = input()

for i in s:
    # 문장을 한글자씩 다 스택에 넣어줍니다.
    st.append(i)
    # print(st)
    # print(p)
    # 스택 길이가 없애야하는 문자보다 길이가 작다면 그냥 넘어가~ 
    if len(st) < len(p):
        continue

    same = True
    #C4를 예를 들면 j는  0,1
    for j in range(len(p)): 
        # print(p[j], st[len(st)- len(p) +j])
        if p[j] != st[len(st)- len(p) +j]:
            same = False
    # 만약에 같다면, C와 4를 pop  하기 
    if same:
        for i in range(len(p)):
            st.pop()

if st:
    print("".join(st))
else:
    print("FRULA")