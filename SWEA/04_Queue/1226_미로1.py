# 1226_미로1

# 16 * 16 행렬
# 가로 x, 세로 y, 미로의 시작점 (1, 1), 도착점 (13, 13)
# 출발점에서 도착점까지 갈 수 있는 길이 있는지 판단
# 가능 여부 1 - 가능, 0 - 불가능

def bfs(si, sj):
    q = []  # queue
    v = [[0] * 16 for _ in range(16)]  # visited

    q.append((si, sj))
    v[si][sj] = 1  # 방문한 곳은 1로 표시

    while q:  # 큐가 비어있지 않으면
        ci, cj = q.pop(0)
        if maze[ci][cj] == 3:  # 도착했다면
            return v[ci][cj]

        # 4방향, 범위 내, 미방문, 1이 아니면(벽이 아닌 경우)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상, 하, 좌, 우
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and v[ni][nj] == 0 and maze[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = 1
    return 0  # 도달할 수 없음을 의미


for tc in range(1, 11):  # 테케 10개
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si, sj = i, j

    ans = bfs(si, sj)
    print(f"#{tc} {ans}")
