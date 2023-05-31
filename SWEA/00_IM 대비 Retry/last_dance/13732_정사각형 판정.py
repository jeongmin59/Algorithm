# 13732_정사각형 판정
def f(N):
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '#':    # 정사각형의 좌상단으로 추측
                k = 1               # '#'이 있는지...
                while i + k < N and j + k < N and lst[i + k][j + k] == '#':   # 대각선으로 크기
                    k += 1
                # 대각선 칸 수 k, 영역 전체가 k인지 확인
                for p in range(i, i + k):       # 내부의 영역 p, q...
                    for q in range(j, j + k):
                        if lst[p][q] == '#':
                            lst[p][q] = '.'
                        else:
                            return 'no'
                return 'yes'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    ans = f(N)

    # 정사각형 외부에 '#'이 있는지 확인
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '#':
                ans = 'no'

    print(f"#{tc} {ans}")
