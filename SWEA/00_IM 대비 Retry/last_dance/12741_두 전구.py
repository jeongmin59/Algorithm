# 12741_두 전구
'''
- 전구 X: A초에서 B초까지, 전구 Y: C초에서 D초까지
- 0초부터 100초까지 전구가 동시에 켜져 있던 시간은 몇 초인지?
'''
T = int(input())
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())

    lst = [0] * 101
    for i in range(A, B + 1):
        lst[i] += 1
    for j in range(C, D + 1):
        lst[j] += 1

    ans = 0
    for k in range(len(lst)):
        if lst[k] == 2:
            ans += 1

    print(f"#{tc} {ans}")
