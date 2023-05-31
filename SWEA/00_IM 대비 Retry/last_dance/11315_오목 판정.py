# 11315_오목 판정

# 우, 우하, 하, 좌하
di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = 'NO'

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(4):
                    cnt = 1         # 오목이니까 0으로 두면 4가 됨
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]

                    if cnt >= 5:
                        ans = 'YES'

    print(f"#{tc} {ans}")
