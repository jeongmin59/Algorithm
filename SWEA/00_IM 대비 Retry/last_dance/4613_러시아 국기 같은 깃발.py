# 4613_러시아 국기 같은 깃발
'''
- W : 흰색, B : 파란색, R: 빨간색
- 한 줄씩 칠해져 한 색으로 있어야 함
- 새로 칠해야 하는 칸의 개수의 최솟값 구하기
'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    minV = N * M

    # WBR 영역 나누기
    for i in range(N - 2):      # W 영역 맨 아래
        for j in range(N - 1):   # B 영역 맨 아래
            cnt = 0
            for p in range(N):
                for q in range(M):
                    if 0 <= p <= i and flag[p][q] != 'W':
                        cnt += 1
                    if i < p <= j and flag[p][q] != 'B':
                        cnt += 1
                    if j < p < N and flag[p][q] != 'R':
                        cnt += 1
            if minV > cnt:
                minV = cnt

    print(f"#{tc} {minV}")