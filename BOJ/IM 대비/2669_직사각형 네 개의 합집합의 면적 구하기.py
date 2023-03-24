# 2669_직사각형 네 개의 합집합의 면적 구하기

# 첫 번째, 두 번째 정수는 사각형 왼쪽 아래 꼭짓점 x, y
# 세 번째, 네 번째 정수는 사각형 오른쪽 위 꼭짓점 x, y

'''
1. 0으로 채워진 빈 배열 만들기
2. 해당 되는 사각형 좌표를 1로 채움
3. 칠해진 부분인 1을 세서 ans에 넣기
'''

lst = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if lst[i][j] == 0:
                lst[i][j] = 1

ans = 0
for k in range(100):
    for l in range(100):
        if lst[k][l] == 1:
            ans += 1

print(ans)
