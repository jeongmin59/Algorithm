# 11399_ATM

N = int(input())
time = list(map(int, input().split()))

time.sort()

cnt = 0
ans = 0

for i in time:
    cnt += i
    ans += cnt

print(ans)
