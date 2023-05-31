# 5789_현주의 상자 바꾸기

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    lst = [0] * (N + 1)

    for q in range(1, Q + 1):
        L, R = map(int, input().split())
        for i in range(L, R + 1):
            lst[i] = q          # 주의

    lst.pop(0)

    print(f"#{tc}", * lst)

