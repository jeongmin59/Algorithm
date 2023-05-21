# 11315_오목 판정
'''
- 가로, 세로, 대각선 중 한 방향으로 5개 이상 연속한 부분 있는지 없는지 판정
- 연속하는 부분이 있으면 'YES', 없으면 'NO'
'''

di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]


def check(lst):
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'o':        # o 이면
                for k in range(4):      # 주변 방향을 체크
                    cnt = 0         # 현재 위치 기준
                    ni = i          # 현재 위치에서 검사 시작 위함
                    nj = j
                    # 범위 벗어 나지 않고, o이 연이어 나오는 거 체크
                    while 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]
                        if cnt == 5:        # 5가 되면 완성!
                            ans = 'YES'
                            return ans
    return ans


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    print(f"#{tc} {check(board)}")
