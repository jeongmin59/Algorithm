# 7102_준홍이의 카드놀이

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    lst = [0] * 41
    for i in range(1, N+1):
        for j in range(1, M+1):
            lst[i + j] += 1

    maxV = max(lst)

    ans = []
    for k in range(len(lst)):
        if lst[k] == maxV:
            ans.append(k)

    print(f"#{tc}", *ans)