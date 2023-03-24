# 14696_딱지놀이
'''
- star: 4, circle: 3, square: 2, triangle: 1
- N: 게임 라운드 수

1. A와 B가 낸 딱지를 list로 받기. 단, 맨 앞의 개수 제외
2. 점수가 가장 큰 모양이 다르다면 큰 모양을 가진 사람이 이김
3. 같다면 개수를 비교
3-1. 다음으로 점수가 큰 모양 비교 및 개수 비교
4. 다 같으면 무승부
'''

N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))[1:]  # 맨 앞 숫자 빼고
    B = list(map(int, input().split()))[1:]

    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):  # 해당 모양의 개수가 A가 많다면
            print("A")
            break
        elif A.count(i) < B.count(i):
            print("B")
            break

        if i == 1:  # 마지막까지 왔는데 break 안 되었으면
            print("D")
