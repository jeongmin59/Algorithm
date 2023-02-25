# 10760_우주선착륙2

# 주변 8개의 방향 중 자신보다 숫자가 작은 방향이 4개의 방향 이상이어야 후보지 선정
# 4개의 방향 이상인 곳의 합 구하기

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    aij = [list(map(int, input().split())) for _ in range(n)]

    # 델타 이용_상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
    di = [-1, 1, 0, 0, -1, 1, -1, 1]
    dj = [0, 0, -1, 1, -1, -1, 1, 1]

    ans = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if aij[ni][nj] < aij[i][j]:     # 나보다 낮은 곳
                        cnt += 1

            if cnt >= 4:    # 4개의 방향 이상인 곳
                ans += 1

    print(f"#{tc} {ans}")
