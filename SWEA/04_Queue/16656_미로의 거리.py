# 16656_미로의 거리

# 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내기
# 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 없는 경우 0을 출력
# 0은 통로, 1은 벽, 2는 출발, 3은 도착 / 미로 밖으로 벗어나면 안됨

def bfs(si, sj):
    q = []  # queue
    v = [[0] * N for _ in range(N)]  # visited

    q.append((si, sj))
    v[si][sj] = 1  # 방문한 곳은 1로 표시

    while q:  # 큐가 비어있지 않으면
        ci, cj = q.pop(0)  # 현재 위치
        if maze[ci][cj] == 3:  # 도착했다면
            return v[ci][cj] - 2  # 2를 빼주고 return

        # 4방향, 범위 내, 미방문이고, 1이 아니면(벽이 아닌 경우)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상, 하, 좌, 우
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and maze[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

    return 0  # 목적지에 도달하지 못한 경우


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    ans = bfs(si, sj)
    print(f"#{tc} {ans}")
