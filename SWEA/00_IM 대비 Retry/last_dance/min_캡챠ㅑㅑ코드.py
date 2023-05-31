# Captcha Code
'''
- sample 코드에서 passcode를 순차적으로 만들 수 있는지 검증
- N : sample 길이, K : passcode 길이
'''

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    i = 0
    ans = 0

    for j in range(N):
        if passcode[i] == sample[j]:
            i += 1
        if i == K:
            ans = 1
            break

    print(f"#{tc} {ans}")