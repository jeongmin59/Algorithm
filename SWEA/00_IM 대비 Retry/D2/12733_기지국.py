# 12733_기지국
'''
- H : 집, X : 아무 것도 없음
- 기지국 A, B, C -> 1, 2, 3씩 커버
- 동, 서, 남, 북으로 커버 되며, 커버되지 않는 집 수 출력
'''

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# num = {'A': 1, 'B': 2, 'C': 3}

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
                    if 0 <= ni < N and 0 <= nj < N:
                        if board[ni][nj] == 'H':
                            board[ni][nj] = 'X'

            elif board[i][j] == 'B':
                for k in range(4):
                    for n in range(1, 3):
                        ni = i + di[k] * n
                        nj = j + dj[k] * n
                        if 0 <= ni < N and 0 <= nj < N:
                            if board[ni][nj] == 'H':
                                board[ni][nj] = 'X'

            elif board[i][j] == 'C':
                for k in range(4):
                    for n in range(1, 4):
                        ni = i + di[k] * n
                        nj = j + dj[k] * n
                        if 0 <= ni < N and 0 <= nj < N:
                            if board[ni][nj] == 'H':
                                board[ni][nj] = 'X'

    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 'H':
                cnt += 1

    print(f"#{tc} {cnt}")
