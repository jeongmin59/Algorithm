# 16107_gravity

# 상자들이 쌓여 있는 방을 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때
# 낙차가 가장 큰 상자를 구하여 낙차를 출력하여라

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    box = list(map(int, input().split()))
    maxV = 0

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if box[i] > box[j]:
                cnt += 1

        if cnt > maxV:
            maxV = cnt

    print(f"#{tc} {maxV}")
