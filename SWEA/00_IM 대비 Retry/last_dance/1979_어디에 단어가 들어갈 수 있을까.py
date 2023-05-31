# 1979_어디에 단어가 들어갈 수 있을까
'''
- 1 : 흰색, 0 : 검은색
'''

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 행부터 볼 때
    ans = 0
    for i in range(N):
        c_cnt = 0
        for j in range(N):
            if board[i][j] == 1:
                c_cnt += 1
            if board[i][j] == 0 or j == N - 1:
                if c_cnt == K:
                    ans += 1
                c_cnt = 0

    # 열 탐색
    for i in range(N):
        r_cnt = 0
        for j in range(N):
            if board[j][i] == 1:
                r_cnt += 1
            if board[j][i] == 0 or j == N - 1:
                if r_cnt == K:
                    ans += 1
                r_cnt = 0

    print(f"#{tc} {ans}")
