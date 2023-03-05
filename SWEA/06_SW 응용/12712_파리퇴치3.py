# 12712_파리퇴치3
'''
- N * N 배열 주어지고, M 범위 만큼의 파리 잡기
- 단, M 범위가 + or x 중 하나로 분사됨
- 한 번에 잡을 수 있는 최대 파리 수 출력
'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 델타_상,하,좌,우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 델타_좌상, 우상, 좌하, 우하
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    catch = []
    for i in range(N):
        for j in range(N):
            sum_ij = 0
            sum_ij += lst[i][j]
            for m in range(1, M):
                for k in range(4):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_ij += lst[ni][nj]

            catch.append(sum_ij)

    for x in range(N):
        for y in range(N):
            sum_xy = 0
            sum_xy += lst[x][y]
            for m in range(1, M):
                for k in range(4):
                    nx = x + dx[k] * m
                    ny = y + dy[k] * m
                    if 0 <= nx < N and 0 <= ny < N:
                        sum_xy += lst[nx][ny]

            catch.append(sum_xy)

    print(f"#{tc} {max(catch)}")

'''
    ans = 0     # 최종 정답
    for i in range(N):
        for j in range(N):
            sum_ij = lst[i][j]  # 상하좌우 합 담을 변수
            sum_xy = lst[i][j]  # 대각선 합 답을 변수
            for k in range(4):
                for m in range(1, M):   # 델타가 이동할 범위
                    ni = i + di[k] * m
                    nj = j + dj[k] * m

                    nx = i + dx[k] * m
                    ny = j + dy[k] * m

                    if 0 <= ni < N and 0 <= nj < N:
                        sum_ij += lst[ni][nj]

                    if 0 <= nx < N and 0 <= ny < N:
                        sum_xy += lst[nx][ny]

            if ans < sum_ij:
                ans = sum_ij
            if ans < sum_xy:
                ans = sum_xy

    print(f"#{tc} {ans}")
'''
