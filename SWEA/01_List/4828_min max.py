# 4828_min max

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

T = int(input())

for i in range(T):
    N = int(input())
    l1 = list(map(int, input().split()))

    l1.sort(reverse=True)

    print(f'#{i + 1} {l1[0] - l1[-1]}')
