# 1652_누울 자리를 찾아라
'''
- . : 아무것도 없는 곳, X : 짐이 있는 곳
- 가로, 세로 2칸 이상의 빈 칸 존재하면 누울 수 있음
- 가로, 세로 누울 수 있는 자리의 수 출력

- 반례...
2
.X
..
- 정답: 1 1

- 생각해 봐야 하는 경우의 수
- 1) 다음 행 또는 열까지 X가 없을 경우 ......
- 2) 최소 칸 수인 2칸만 있을 경우 ..X..X
- 3) 나머지 (보통의 경우) ...X.X
'''

N = int(input())
room = [list(str(input())) for _ in range(N)]

r_ans = []
c_ans = []

for i in range(N):
    r_cnt, c_cnt = 0, 0
    for j in range(N):
        if room[i][j] == '.':
            r_cnt += 1
        elif room[i][j] == 'X':
            if r_cnt >= 2:
                r_ans.append(r_cnt)
            r_cnt = 0

        if room[j][i] == '.':
            c_cnt += 1
        elif room[j][i] == 'X':
            if c_cnt >= 2:
                c_ans.append(c_cnt)
            c_cnt = 0

    if r_cnt >= 2:
        r_ans.append(r_cnt)
    if c_cnt >= 2:
        c_ans.append(c_cnt)

print(len(r_ans), len(c_ans))
