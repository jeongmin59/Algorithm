# 2578_빙고
'''
- 5 * 5 빙고판이며 가로, 세로, 대각선 포함해서 3줄 이상 빙고
- 빙고판과 숫자를 돌면면서 숫자가 선언되면 빙고판에서 숫자 remove
- 빙고판이 [] 빈 리스트가 되면 1씩 올려주고 3이 되면 break
'''

board1 = [list(map(int, input().split())) for _ in range(5)]    # 원래 빙고판 (가로 빙고)
board2 = list(map(list, zip(*board1)))  # 전치 행렬 (세로 빙고)

board3 = []
board4 = []
for i in range(len(board1)):
    board3.append(board1[i][i])     # 왼쪽 대각선 빙고
    board4.append(board2[i][4 - i]) # 오른쪽 대각선 빙고

board = board1 + board2
board.append(board3)
board.append(board4)

num = []
for _ in range(5):
    num += list(map(int, input().split()))

ans = 0
for i in num:
    ans += 1
    bingo = 0
    for j in board:
        if i in j:
            j.remove(i)
        if j == []:
            bingo += 1
    if bingo >= 3:
        break

print(ans)

