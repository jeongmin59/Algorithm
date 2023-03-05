# 2805_농작물 수확하기
'''
- 농장의 크기는 항상 홀수: 1, 3, 5, 7, ..., 49
- 수확은 항상 농장의 크기에 맞는 정사각형 마름모 형태로만 가능
* key point
- 시작점, 끝점, 인덱스, 중간 값 찾기
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    ans = 0
    s = e = N // 2      # s: 시작점, e: 끝점

    for i in range(N):
        for j in range(s, e+1):
            ans += farm[i][j]

        if i < N // 2:
            s -= 1
            e += 1

        else:
            s += 1
            e -= 1

    print(f"#{tc} {ans}")
