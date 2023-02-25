# 16268_풍선팡2

# 풍선의 상, 하, 좌, 우, 가운데의 합을 구하고, 합들 중 최대값을 출력
# n * m 크기

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(n)]

    # 델타 이용_상, 하, 좌, 우
    di = [-1, 1, 0, 0, 0]
    dj = [0, 0, -1, 1, 0]

    max_p = 0   # 합들 중 제일 큰 값
    for i in range(n):
        for j in range(m):
            pang = 0        # 터진 풍선 꽃가루의 합
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    pang += balloon[ni][nj]
                    if max_p < pang:
                        max_p = pang

    print(f"#{tc} {max_p}")
