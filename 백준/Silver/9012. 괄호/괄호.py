
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif not stack or stack.pop() != p:
            return False
    return not stack


n = int(input())

for _ in range(n):
    input_list = list(input())

    if isValid(input_list) == True:
        print("YES")
    else:
        print("NO")
