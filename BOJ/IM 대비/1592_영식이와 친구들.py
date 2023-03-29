# 1592_영식이와 친구들
'''
- 나머지를 이용한 방향 지정...

'''


N, M, L = map(int, input().split())

game = [0 for _ in range(N)]

cnt = 0     # 공을 주고 받는 횟수
idx = 0

while True:
    game[idx] += 1
    if game[idx] == M:
        print(cnt)
        break
    elif game[idx] % 2 != 0:    # 홀수
        idx = (idx + L) % N
    else:
        idx = (idx + N - L) % N
    cnt += 1
