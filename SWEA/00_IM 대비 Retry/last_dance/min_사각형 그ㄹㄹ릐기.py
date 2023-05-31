# 사각형 그리기 게임
'''
- 최대한 면적이 큰 사각형 몇 개 그릴 수 있는지?
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    maxC = 0

    for i in range(N):
        for j in range(N):
            cur = board[i][j]   # 왼쪽 상단
            for p in range(i, N):
                for q in range(j, N):
                    if cur == board[p][q]:
                        square = (p - i + 1) * (q - j + 1)
                        if maxV < square:
                            maxV = square
                            maxC = 1
                        elif maxV == square:
                            maxC += 1
    print(f"#{tc} {maxC}")
