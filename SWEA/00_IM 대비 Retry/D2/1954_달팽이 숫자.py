# 1954_달팽이 숫자
'''
- N * N 배열 시계 방향으로 회전된 달팽이 출력!
'''
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [[0] * N for _ in range(N)]

    i, j = 0, 0     # 시작 위치
    cnt = 1
    k = 0

    while cnt <= N * N:
        lst[i][j] = cnt     # 현재 위치
        cnt += 1
        ni, nj = i + di[k], j + dj[k]
        if (0 <= ni < N) and (0 <= nj < N) and lst[ni][nj] == 0:
            i, j = ni, nj   # 현재 위치를 업데이트
        else:
            k = (k + 1) % 4 # 방향 바꾸기
            ni, nj = i + di[k], j + dj[k]   # 새로운 방향으로 계산
            i, j = ni, nj   # 현재 위치 업데이트

    print(f"#{tc}")
    for x in lst:
        print(*x)

'''
# 이전 풀이
T = int(input())

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]

    i, j = 0, -1

    cnt = 1
    k = 0   # 방향 - 우, 하, 좌, 상

    while cnt <= N * N:
        ni = i + di[k]
        nj = j + dj[k]

        if (0 <= ni < N) and (0 <= nj < N) and snail[ni][nj] == 0:
            snail[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj       # 현재 위치 갱신

        else:
            k = (k + 1) % 4

    print(f"#{tc}")
    for x in snail:
        print(*x)
'''
