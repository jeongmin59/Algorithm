# 5789_현주의 상자 바꾸기
'''
- 숫자 카드와 유사
'''
T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    lst = [0] * (N + 1)

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            lst[j] = i

    lst.pop(0)

    print(f"#{tc}", *lst)

'''
# 이전 풀이 - 이게 더 시간이 빠름
T = int(input())
 
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N
 
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box[j] = i
 
    print(f"#{tc}", *box)
'''
