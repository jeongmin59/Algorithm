# 1954_달팽이 숫자

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    # 2차원 빈 배열
    arr = [[0 for _ in range(n)] for _ in range(n)]
    # 델타 - 우, 하, 좌, 상
    di = [0, 1, 0, -1]  # 하, 상
    dj = [1, 0, -1, 0]  # 우, 좌

    i, j = 0, -1

    cnt = 1
    k = 0

    while cnt <= n * n:
        ni = i + di[k]
        nj = j + dj[k]

        if (0 <= ni < n) and (0 <= nj < n) and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj

        else:  # 방향 바꿈
            k = (k + 1) % 4

    print(f"#{tc}")
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")

        print()
