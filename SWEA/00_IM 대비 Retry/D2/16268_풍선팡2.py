# 16268_풍선팡2
'''
- N * M
- 가운데 풍선을 터뜨리면 상, 하, 좌, 우 풍선이 추가로 터지면서 5개의 꽃가루가 날림
- 한 개의 풍선을 터뜨렸을 때 날릴 수 있는 꽃가루 중 최대값 출력
'''

di = [-1, 1, 0, 0, 0]
dj = [0, 0, -1, 1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    maxV= 0
    for i in range(N):
        for j in range(M):
            pang = 0
            for k in range(5):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    pang += board[ni][nj]
                    if maxV < pang:
                        maxV = pang

    print(f"#{tc} {maxV}")
