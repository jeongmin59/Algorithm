# 10163_색종이

'''
- 주어진 순서대로 색종이가 놓이게 되고, 가져진 부분을 제외한 색종이가 보이는 부분의 면적 출력
'''

N = int(input())
board = [[0 for _ in range(1001)] for _ in range(1001)]

for k in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x + w):
        for j in range(y, y + h):
            board[i][j] = k


for k in range(1, N + 1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == k:
                cnt += 1

    print(cnt)

