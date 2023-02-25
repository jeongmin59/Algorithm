# 13702_델타 검색

# 상, 하, 좌, 우로 이웃한 요소와의 차의 절대값을 구하고 이 값들의 합을 구하기
# n * n 리스트

for tc in range(1, 11):     # tc의 개수 10개
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    # 델타 이용_상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    s_sum = 0       # 차들의 총합
    for i in range(n):
        for j in range(n):
            sub = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    sub += abs(lst[i][j] - lst[ni][nj])     # 차의 절대값
            s_sum += sub

    print(f"#{tc} {s_sum}")
