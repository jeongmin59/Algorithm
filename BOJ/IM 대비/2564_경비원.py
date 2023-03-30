# 2564_경비원
'''
- 현재 위치와 각 상점 사이의 최단 거리의 합 출력
- 1, 2 는 북, 남 / 3, 4는 서, 동
'''

def get_d(x, y):
    if x == 1:  # 북
        return y
    if x == 2:  # 남
        return w + h + w - y
    if x == 3:  # 서
        return w + h + w + h - y
    if x == 4:  # 동
        return w + y

w, h = map(int, input().split())    # 가로, 세로
n = int(input())

course = []
for _ in range(n + 1):      # 북, 왼 시작지점에서 상점까지
    x, y = map(int, input().split())
    course.append(get_d(x, y))

ans = 0

for i in range(n):  # 동근이와 상점 사이 최단 거리
    in_c = abs(course[-1] - course[i])  # 시계 방향
    out_c = 2 * (w + h) - in_c  # 반시계 방향
    ans += min(in_c, out_c) # 두 개 중 작은 값

print(ans)
