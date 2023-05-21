# 1979_어디에 단어가 들어갈 수 있을까
'''
- N * N 배열, 1 : 흰색, 0 : 검은색
- K의 길이에 맞는 칸이 몇 개인지 출력
'''
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    cnt = 0
    # 가로
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1
            if board[i][j] == 0 or j == N - 1:
                if cnt == K:
                    ans += 1
                cnt = 0

    # 세로
    for i in range(N):
        for j in range(N):
            if board[j][i] == 1:
                cnt += 1
            if board[j][i] == 0 or j == N - 1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f"#{tc} {ans}")
