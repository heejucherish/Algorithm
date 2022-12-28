for _ in range(int(input())):

    blank = input()
    box = []
    candy = 0

    r, c = map(int, input().split())
    for _ in range(r):
        box += input().split()


    for i in range(r):
        for j in range(c-2):
            if box[i][j: j+3] == ">o<":
                candy +=1

    for i in range(r-2):
        for j in range(c):
            vertical = box[i][j] +box[i+1][j] + box[i+2][j]
            if vertical =="vo^":
                candy += 1

    print(candy)