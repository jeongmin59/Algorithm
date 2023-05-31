# 9489_고대 유적
'''
- 1로 된 구조물 중 가장 긴 구조물의 길이 출력
- 행과 열을 탐색, 대각선은 해당 X
- N * M 배열
* 풀이
- 행과 열을 탐색하면서 1을 만났을 때 cnt += 1, 0을 만나면 초기화 되어야 함
- 숫자를 센 것 중에서 가장 큰 값과 비교
'''
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 행
    maxV = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
                if maxV <= cnt:
                    maxV = cnt
            else:
                cnt = 0
    # 열
    for i in range(M):
        cnt = 0
        for j in range(N):
            if board[j][i] == 1:
                cnt += 1
                if maxV <= cnt:
                    maxV = cnt
            else:
                cnt = 0

    print(f"#{tc} {maxV}")

'''
row_maxV, col_maxV로 따로 두고 했을 때 런타임 에러 발생 -> 왜지?
ans = max(row_maxV, col_maxV)로 뒀는데...?
'''
