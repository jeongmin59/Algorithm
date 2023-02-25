# 9368_연속한 1의 개수

# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대 값을 출력
# 첫 줄에 테스트 케이스 개수 T, 다음 줄에는 수열의 길이 N
# 다음 줄에는 N개의 0과 1로 구성된 수열이 공백 없이 제공

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input()))

    one_lst = []
    cnt = 0
    for i in range(n):
        if lst[i] == 1:
            cnt += 1
            one_lst.append(cnt)     # 1이 있고, 또 더하면 2가 된 그 상태를 더하는
        elif lst[i] == 0:
            cnt = 0                 # 0일때 0으로 초기화

    print(f'#{tc} {max(one_lst)}')
