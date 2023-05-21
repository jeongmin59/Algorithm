# 1204_최빈수 구하기
'''
- 학생 수 1000명, 점수는 0점 이상 100점 이하 값
- 최빈값 출력
'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    lst = [0] * 101

    for s in score:
        lst[s] += 1

    maxV = 0
    maxIdx = 0
    for i in range(len(lst)):
        if maxV <= lst[i]:
            maxV = lst[i]
            maxIdx = i

    print(f"#{tc} {maxIdx}")
