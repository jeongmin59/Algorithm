# 16918_화물 도크

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    time.sort(key=lambda x: x[1])

    # print(time)
    cnt = now = 0

    for i in range(N):
        s = time[i][0]
        e = time[i][1]
        if now <= s:
            cnt += 1
            now = e

    print(f"#{tc} {cnt}")
