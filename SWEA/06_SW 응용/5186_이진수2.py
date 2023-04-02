T = int(input())
for tc in range(1, T + 1):
    N = float(input())

    cnt = 0
    ans = ''     # 2진수 저장
    while N > 0:
        N = N * 2

        if N >= 1:
            ans += "1"
            N -= 1

        elif N < 1:
            ans += "0"

        if len(ans) > 13:
            ans = "overflow"
            break

    print(f"#{tc} {ans}")
