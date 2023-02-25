# 1206_View

T = 10

for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    view = 0
    for i in range(2, N - 2):  # 양쪽 옆이 0이기 때문. end +1
        maxV = 0
        for j in range(i - 2, i + 3):
            if i != j and maxV < li[j]:
                maxV = li[j]
        if li[i] > maxV:  # 조망권 확보
            view += li[i] - maxV
    print(f'#{tc} {view}')
