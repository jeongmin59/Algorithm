# 16889_전자카트

def dfs(n, sm, cur):
    global ans
    if ans <= sm:
        return

    if n == N:
        # 여태까지의 소모량 + 1번으로 복귀비용
        ans = min(ans, sm + lst[cur][1])
        return

    for j in range(2, N + 1):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, sm + lst[cur][j], j)
            v[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    v = [0] * (N + 1)
    ans = 100 * N
    dfs(1, 0, 1)

    print(f'#{tc} {ans}')