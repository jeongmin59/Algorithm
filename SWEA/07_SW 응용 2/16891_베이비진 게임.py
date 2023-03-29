# 16891_베이비진 게임

def check(player):
    for j in range(10):
        if player[j] == 3:
            return True
    for k in range(8):  # 마지막 7, 8, 9까지만 검사
        if player[k] and player[k + 1] and player[k + 2]:
            return True
    return False    # 승리요건 달성 못 함

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 각각의 인덱스가 카드 번호가 되도록 플레이어들 초기값 생성
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    for i in range(len(cards)):
        if i % 2 == 0:
            p1[cards[i]] += 1
            if check(p1):
                winner = 1
                break
        else:
            p2[cards[i]] += 1
            if check(p2):
                winner = 2
                break

    print(f"#{tc} {winner}")
