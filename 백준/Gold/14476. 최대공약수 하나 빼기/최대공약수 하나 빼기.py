import sys, math

# 입력부
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# pf_gcd : 0부터 i까지의 gcd를 저장하는 리스트
# sf_gcd : i부터 n - 1까지의 gcd를 저장하는 리스트
pf_gcd = [0] * (n + 1)
sf_gcd = [0] * (n + 1)

pf_gcd[0] = arr[0]
for i in range(1, n):
    pf_gcd[i] = math.gcd(pf_gcd[i - 1], arr[i])
sf_gcd[n - 1] = arr[n - 1]
for i in range(n - 2, -1, -1):
    sf_gcd[i] = math.gcd(sf_gcd[i + 1], arr[i])
    
# ans : 정답 배열
ans = []
for i in range(n):
    # left : [0, i - 1]까지의 gcd
    left = pf_gcd[i - 1]
    # right : [i + 1, n - 1]까지의 gcd
    right = sf_gcd[i + 1]
    # res : i번째 수를 제외한 최종 gcd
    res = math.gcd(left, right)
    # 약수가 아니라면 정답 배열에 저장
    if arr[i] % res == 0:
        continue
    ans.append((res, arr[i]))
    
# 정렬 후 정답출력
ans.sort(reverse=True)
print(' '.join(map(str, ans[0])) if ans else -1)