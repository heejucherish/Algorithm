'''
n개의 화분을 k만큼의 수분을 갖도록 초기화 하자.
화분의 수분이 0이 아닐 동안, 반복하면서 a개의 화분에 b씩 물을 주자.
모든 화분의 수분을 1씩 감소시키자.
화분의 수분이 적은 순으로 정렬하자.(그래야 매 반복마다 제일 수분이 적은 a개의 화분에 b씩 수분을 줄 수 있음.)
day를 1 증가시키자.

'''
# 6 3 2 2 


def watering(n, k, a, b):
    arr = [k] * n

    day = 0
    while 0 not in arr:

        # A개의 화분에 B씩 물주기
        for i in range(a):
            arr[i] += b

        # 모든 화분의 수분이 1씩 감소
        for i in range(len(arr)):
            arr[i] -= 1

        # 수분이 적은 순으로 재 정렬
        arr.sort()
        day += 1

    return day


n, k, a, b = map(int, input().split())
print(watering(n, k, a, b))