# 1220_Magnetic
T = 10
for tc in range(1, T + 1):
    table = int(input())
    lst = [list(map(int, input().split())) for _ in range(table)]

    N = 1
    S = 2

    # 열 우선 순회
    cnt = 0             # 교착점 개수
    for i in range(100):
        start = 0       # N극 유무
        for j in range(100):
            if lst[j][i] == N:
                start = 1
            elif lst[j][i] == S:      # S극인 경우
                if start:           # N극 아래면
                    cnt += 1
                    start = 0

    print(f"#{tc} {cnt}")

