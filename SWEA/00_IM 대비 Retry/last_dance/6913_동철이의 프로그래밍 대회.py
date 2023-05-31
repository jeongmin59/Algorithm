# 6913_동철이의 프로그래밍 대회
'''
- N명의 사람, M개의 문제
- 1등한 사람의 수와 1등이 푼 문제 수 출력
'''
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, (input().split()))
    score = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    maxC = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if score[i][j] == 1:
                cnt += 1
        if maxV < cnt:
            maxV = cnt
            maxC = 1
        elif maxV == cnt:
            maxC += 1

    print(f"#{tc} {maxC} {maxV}")
