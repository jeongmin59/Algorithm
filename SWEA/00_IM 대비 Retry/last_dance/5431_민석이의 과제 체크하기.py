# 5431_민석이의 과제 체크하기
'''
- N : 수강생 수, K : 과제 제출한 사람 수
- 제출하지 않은 사람의 번호를 오름차순으로 출력
'''
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, (input().split()))
    num = list(map(int, input().split()))

    lst = []
    for i in range(1, N + 1):
        if i not in num:
            lst.append(i)

    print(f"#{tc}", *lst)
