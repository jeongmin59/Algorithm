# 차르봄바
'''
- 최대한 많은 바이러스를 제거했을 때 제거된 바이러스의 수 출력
'''

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    garden = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            cnt = garden[i][j]      # 현재 위치로
            for p in range(1, P + 1):
                for k in range(4):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += garden[ni][nj]
            if maxV < cnt:
                maxV = cnt

    print(f"#{tc} {maxV}")

