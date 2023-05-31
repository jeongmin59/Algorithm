# 3499_퍼펙트 셔플

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = input().split()

    mid = (N + 1) // 2      # 두 번째 덱의 첫 인덱스

    print(f"#{tc}", end=' ')
    for i in range(N // 2):
        print(lst[i], lst[i+mid], end=' ')
    if N % 2:       # 홀수 개인 경우
        print(lst[N // 2])
    else:
        print()
