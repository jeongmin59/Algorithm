# 1209_sum
'''
- 대각선의 합...구하는게 쉽지 않네
'''

T = 10
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합
    col_max = 0
    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt += board[i][j]
            if col_max < cnt:
                col_max = cnt

    # 열의 합
    row_max = 0
    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt += board[j][i]
            if row_max < cnt:
                row_max = cnt

    # 좌상-우하 대각선의 합
    line1 = 0
    for i in range(100):
        line1 += board[i][i]

    # 우상-좌하 대각선의 합
    line2 = 0
    for i in range(100):
        line2 += board[i][99-i]

    maxV = max(col_max, row_max, line1, line2)

    print(f"#{tc} {maxV}")
