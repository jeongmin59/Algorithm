# 11315_오목 판정
'''
- 가로, 세로, 대각선 중 하나의 방향으로 5개 이상
- o : 돌, . : 돌 X
- 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래 순서로
di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]
'''

def check(board):
    for i in range(N):
        for j in range(N):
            for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1)):
                for mul in range(5):
                    ni, nj = i + di * mul, j + dj * mul
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                        pass
                    else:
                        break
                else:
                    return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    ans = check(board)

    print(f"#{tc} {ans}")