# 16811_당근 포장하기

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    minV = N

    for i in range(N-2):    # 소
        for j in range(i+1, N-1):   # 중, 대 j+1 ~ N-1
            # 같은 크기 당근이 다른 포장에 들어가는 경우 제외
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                s = carrot[:i+1]
                m = carrot[i+1:j+1]
                l = carrot[j+1:]

                if len(s) <= N // 2 and len(m) <= N // 2 and len(l) <= N // 2:
                    if minV > max(len(s), len(m), len(l)) - min(len(s), len(m), len(l)):
                        minV = max(len(s), len(m), len(l)) - min(len(s), len(m), len(l))

    if minV == N:
        minV = -1

    print(f"#{tc} {minV}")
