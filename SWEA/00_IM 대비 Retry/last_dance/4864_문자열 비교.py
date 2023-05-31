# 4864_문자열 비교
T = int(input())
for tc in range(1, T + 1):
    st1 = input()
    st2 = input()
    st1_l = len(st1)
    st2_l = len(st2)

    ans = 0
    for j in range(st2_l - st1_l):
        for i in range(st1_l):
            if st1[i] != st2[j+i]:
                break
            if i == st1_l - 1:
                ans = 1
        if ans == 1:
            break

    print(f"#{tc} {ans}")

    # ans = 0
    # # st2 안에 st1이 포함되어 있는지 확인
    # i = 0       # j와 비교할 st1 인덱스
    # for j in range(st2_l):
    #     if st1[i] == st2[j]:
    #         i += 1
    #         if i == st1_l:
    #             ans = 1
    #             break
    #     else:
    #         i = 0
    #         if st1[i] == st2[j]:        # ZZZZAABCZZZZ 이런 식일 때 주의
    #             i += 1
    #
    # print(f"#{tc} {ans}")


