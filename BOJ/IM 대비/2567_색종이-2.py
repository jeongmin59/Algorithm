# 2567_색종이 - 2
'''
- 색종이의 둘레 길이 출력
'''

N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j] == 1:
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if paper[ni][nj] == 1:
                    cnt += 1
            if cnt == 3:
                ans += 1
            elif cnt == 2:
                ans += 2
print(ans)

