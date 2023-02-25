# 4834_숫자 카드

# 0에서 9까지 숫자가 적힌 N장의 카드가 주어짐
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    card = list(map(int, input()))
    cnt = [0] * 10

    for i in range(N):
        cnt[int(card[i])] += 1

    max_cnt = 0

    for j in range(len(cnt)):
        if max_cnt <= cnt[j]:
            max_cnt = cnt[j]
            result = j

    print(f'#{t} {result} {max_cnt}')
