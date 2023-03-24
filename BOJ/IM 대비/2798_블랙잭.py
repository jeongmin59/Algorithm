# 2798_블랙잭
'''
- N장의 카드가 주어졌을 때, M을 넘지 않으면 M에 최대한 가까운 카드 3장의 합
'''

N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_card = cards[i] + cards[j] + cards[k]
            if sum_card <= M:
                if ans < sum_card:
                    ans = sum_card

print(ans)
