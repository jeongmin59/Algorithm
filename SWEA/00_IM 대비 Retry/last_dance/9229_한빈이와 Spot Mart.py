# 9229_한빈이와 Spot Mart
'''
- M이하 중 합이 가장 큰 과자 2개 고르기
- 들고 갈 방법이 없는 경우에는 -1 출력
'''
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    snack = list(map(int, input().split()))

    maxV = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            if snack[i] + snack[j] <= M:
                if maxV < snack[i] + snack[j]:
                    maxV = snack[i] + snack[j]

    print(f"#{tc} {maxV}")

