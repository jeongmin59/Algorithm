# 5948_새샘이의 7-3-5 게임
'''
- 서로 다른 7개의 정수 중 3개의 정수를 골라 합을 구해서 수를 만들 때
- 5번째로 큰 수를 출력하는 프로그램 작성
'''

T = int(input())
for tc in range(1, T + 1):
    num = list(map(int, input().split()))

    s = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                s.append(num[i] + num[j] + num[k])

    s = list(set(s))
    s.sort()

    print(s)
