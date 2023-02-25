# 16636_회전 문제(회전)

# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때
# 맨 앞에 있는 숫자 출력

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for m in range(M):
        queue.append(queue[0])
        queue.pop(0)

    print(f"#{tc} {queue[0]}")
