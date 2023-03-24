# 10709_기상캐스터
'''
- 입력은 구름이 있는 경우 'c'로 주어지고 없는 경우 '.'으로 주어짐
- 처음부터 구역에 구름이 있는 경우 0을 출력, 몇 분이 지나도 뜨지 않을 경우 -1을 출력해야 함

1. 빈 리스트 만들기
2. 입력 받은 리스트를 순회 하면서 다음의 조건에 맞게 값 바꾸기
- cnt를 -1로 설정
- 만약 입력 받은 리스트의 값이 c라면 cnt = 0
- cnt가 0보다 크거나 같을 경우 + 1 아니면 그대로 -1
- 빈 리스트에 cnt 값으로 대체 하기
'''

H, W = map(int, input().split())
c_lst = [list(input()) for _ in range(H)]
cloud = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    cnt = -1    # "c"를 만나지 못하면 계속 -1
    for j in range(W):
        if c_lst[i][j] == "c":
            cnt = 0
        else:
            if cnt >= 0:
                cnt += 1
        cloud[i][j] = cnt

for c in cloud:
    print(*c)

