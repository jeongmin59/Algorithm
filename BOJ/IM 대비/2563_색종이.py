# 2536_색종이
'''
- 가로, 세로 크기가 100인 도화지에 가로, 세로 10인 색종이를 붙임
- 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램 작성
- 첫 번째 자연수는 색종이의 왼쪽 변, 도화지 왼쪽 변 사이의 거리
- 두 번째 자연수는 색종이의 아래쪽 변, 도화지 아래쪽 변 사이의 거리

1. 100 * 100 빈 배열 만들기
2. 빈 배열에 해당 되는 좌표 색칠
3. 숫자가 1인 것들을 세는 것이 답
'''

n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]   # 도화지

for _ in range(n):
    x, y = map(int, input().split())

    ans = 0
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if paper[i][j] == 0:
                paper[i][j] = 1

    for i in range(100):
        for j in range(100):
            if paper[i][j] == 1:
                ans += 1

print(ans)

