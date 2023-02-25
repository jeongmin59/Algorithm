# 1217_거듭 제곱

for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())


    def power(n, m):
        if m < 1:
            return 1
        else:
            return n * power(n, m - 1)


    print(f"#{t} {power(n, m)}")
