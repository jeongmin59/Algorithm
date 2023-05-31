# 4615_재미있는 오셀로 게임
'''
- 1 : 흑돌, 2 : 백돌
'''

# 오른쪽 부터 시계 방향
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * (N + 1) for _ in range(N + 1)]   # 1번 인덱스 부터

    B = 1
    W = 2

    board[N // 2][N // 2] = W
    board[N // 2][N // 2 + 1] = B
    board[N // 2 + 1][N // 2] = B
    board[N // 2 + 1][N // 2 + 1] = W

    for _ in range(M):
        col, row, color = map(int, input().split())

        board[row][col] = color
        for k in range(8):
            ni = row + di[k]
            nj = col + dj[k]
            lst = []
            while 1 <= ni <= N and 1 <= nj <= N and board[ni][nj] != 0:
                if board[ni][nj] != color:      # 색이 다를 때
                    lst.append((ni, nj))
                    ni = ni + di[k]
                    nj = nj + dj[k]
                else:   # 같으면 저장한 돌 뒤집기...
                    for x, y in lst:
                        board[x][y] = color
                    break

    cnt_B = 0
    cnt_W = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == B:
                cnt_B += 1
            elif board[i][j] == W:
                cnt_W += 1

    print(f"#{tc} {cnt_B} {cnt_W}")
