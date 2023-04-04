# 2491_수열
'''
- 0에서부터 9까지의 숫자로 이루어진 N개의 숫자...
- 수열 안에서 연속해서 커지거나 연속해서 작아지는 수열 중 가장 길이가 긴 것 출력 (같은 것도 포함한다.)
- 연속해서 커지거나 작아지는 수열의 길이가 3이상인 경우가 없으면 2 출력

- 증가하는 수열, 감소하는 수열 구해야 함
'''

N = int(input())
lst = list(map(int, input().split()))

up_dp = [1] * N
down_dp = [1] * N

for i in range(1, N):
    if lst[i - 1] <= lst[i]:
        up_dp[i] = up_dp[i - 1] + 1

    if lst[i - 1] >= lst[i]:
        down_dp[i] = down_dp[i - 1] + 1

max1 = max(up_dp)
max2 = max(down_dp)

print(max(max1, max2))
