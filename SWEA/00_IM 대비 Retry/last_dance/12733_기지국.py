# 기지국
'''
- A : 1, B : 2, C : 3, 집 : H
'''

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'A':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'H':
                        board[ni][nj] = 'X'

            elif board[i][j] == 'B':
                for p in range(1, 3):
                    for k in range(4):
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'H':
                            board[ni][nj] = 'X'

            elif board[i][j] == 'C':
                for p in range(1, 4):
                    for k in range(4):
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'H':
                            board[ni][nj] = 'X'

    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 'H':
                cnt += 1

    print(f"#{tc} {cnt}")
