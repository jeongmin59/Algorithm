# 4835_구간합

# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    l1 = list(map(int, input().split()))

    sum_list = []

    for j in range(N - M + 1):  # 구간합!!!
        sum_ = sum(l1[j: j + M])  # l1[j:j+M] 한 칸씩 옮겨가며 출력
        sum_list.append(sum_)

    print(f'#{i + 1} {max(sum_list) - min(sum_list)}')
