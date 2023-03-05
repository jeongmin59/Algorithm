# 1220_Magenetic
'''
- 1은 N극, 2는 S극
- 100 * 100

- 빈칸(무시), 1, 2의 경우 파란색(2)을 찾고 직전 값이 1인 경우 교착 상태
- 직전 색을 갱신하면 됨 (1인지 2인지)
- 전치 행렬을 통해 열을 행으로 바꿈
'''

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        flag = 0        # 교착 확인을 위한 변수
        for j in range(N):
            if lst[j][i] == 1:
                flag = 1
            elif lst[j][i] == 2:
                if flag:
                    ans += 1
                    flag = 0


    # 문어 박사님 코드
    # ans = 0
    # n_lst = list(zip(*lst))     # 전치 행렬
    # for l in n_lst:             # 행 단위로 처리
    #     prev = 0        # 직전 색
    #     for n in l:
    #         if n:       # 0이 아닌 경우만 처리
    #             if n == 2 and prev == 1:
    #                 ans += 1
    #             prev = n

    print(f"#{tc} {ans}")
