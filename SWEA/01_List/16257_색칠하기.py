# 16257_색칠하기

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    zro = [[0 for _ in range(10)] for _ in range(10)]

    cnt = 0
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if zro[i][j] != color and zro[i][j] < 3:
                    zro[i][j] += color
                if zro[i][j] == 3:
                    cnt += 1

    print(f"#{tc} {cnt}")
