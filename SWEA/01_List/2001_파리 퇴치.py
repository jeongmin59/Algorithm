# 2001_파리 퇴치

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    max_d = 0  # 최대값 저장
    for si in range(0, n - m + 1):  # 시작 좌표
        for sj in range(0, n - m + 1):
            dead = 0  # 초기화
            for i in range(si, si + m):  # 파리채 범위
                for j in range(sj, sj + m):
                    dead += lst[i][j]  # 파리의 개수 저장
            if max_d < dead:
                max_d = dead

    print(f"#{tc} {max_d}")
