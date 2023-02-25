# 1209_Sum

# 2차원 배열의 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값 구하기

for tc in range(1, 11):
    t = int(input())    # tc 번호
    lst = [list(map(int, input().split())) for _ in range(100)]

    # 각 행의 합 i
    max_i = 0
    for i in range(100):
        sum_i = 0
        for j in range(100):
            sum_i += lst[i][j]
            if max_i < sum_i:
                max_i = sum_i

    # 각 열의 합 j
    max_j = 0
    for i in range(100):
        sum_j = 0
        for j in range(100):
            sum_j += lst[j][i]
            if max_j < sum_j:
                max_j = sum_j

    # 좌상-우하 대각선의 합
    sum_l = 0
    for i in range(100):
        sum_l += lst[i][i]

    # 우상-좌하 대각선의 합
    sum_r = 0
    for i in range(99, 0, -1):
        sum_r += lst[i][i]

    print(f"#{tc} {max(max_i, max_j, sum_l, sum_r)}")
