# 4834_숫자 카드
'''
- 0 ~ 9까지 적힌 숫자 카드
- 가장 많은 카드에 적힌 숫자와 카드 몇 장인지 출력
- 단, 장수가 같을 때는 적힌 숫자가 큰 쪽 출력
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input()))
    lst = [0] * 10

    for c in card:
        lst[c] += 1

    maxV = 0
    maxIdx = 0

    for i in range(len(lst)):
        if maxV <= lst[i]:
            maxV = lst[i]
            maxIdx = i

    print(f"#{tc} {maxIdx} {maxV}")
