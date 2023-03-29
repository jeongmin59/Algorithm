# 16917_컨테이너 운반

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort()
    truck.sort()

    ans = 0
    while weight and truck:
        if truck[-1] >= weight[-1]:
            truck.pop()
            ans += weight.pop()
        else:
            weight.pop()

    print(f"#{tc} {ans}")

