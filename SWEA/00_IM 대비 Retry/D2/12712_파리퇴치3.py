# 12712_파리퇴치3
'''
- N * N 배열, M의 세기로 분사 + 또는 x 중 하나로 분사됨
- 한 번에 잡을 수 있는 최대 파리 수 출력
'''

# + 방향 : 0 ~ 3, x 방향 : 4 ~ 8
di = [0, 1, 0, -1, -1, 1, 1, -1]
dj = [1, 0, -1, 0, 1, 1, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = board[i][j]   # 시작 위치
            for k in range(4):
                for m in range(1, M):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += board[ni][nj]
            if ans < cnt:
                ans = cnt

            cnt = board[i][j]
            for k in range(4, 8):
                for m in range(1, M):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += board[ni][nj]
            if ans < cnt:
                ans = cnt

    print(f"#{tc} {ans}")

