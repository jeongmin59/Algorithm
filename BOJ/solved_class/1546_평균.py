# 1546_평균
'''
- 새로운 점수 계산 = 점수 / max점수 * 100
- 새로운 평균 구하는 프로그램 작성하기
'''

N = int(input())
score = list(map(int, input().split()))

M = max(score)
new_s = 0

for i in score:
    if i == M:
        new_s += 100    # M/M*100 = 100
    else:
        new_s += (i / M * 100)

average = new_s / N

print(average)
