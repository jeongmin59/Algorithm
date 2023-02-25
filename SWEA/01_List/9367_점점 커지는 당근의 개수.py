# 9367_점점 커지는 당근의 개수

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    c = list(map(int, input().split()))

    cnt = 1
    c_lst = []

    for i in range(1, n):       # 인덱스 0 ~ 4
        if c[i-1] >= c[i]:
            cnt = 1             # 구간 최소 길이 == 1
            c_lst.append(cnt)
        else:
            cnt += 1
            c_lst.append(cnt)

    print(f'#{tc} {max(c_lst)}')
