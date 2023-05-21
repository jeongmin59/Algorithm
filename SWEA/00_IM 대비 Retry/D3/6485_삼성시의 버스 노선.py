# 6485_삼성시의 버스 노선
'''
- 5000개의 정류장 1에서 5000까지 번호 붙어 있음 -> 빈 리스트 5001
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            lst[i] += 1

    P = int(input())
    bus_stop = []
    for _ in range(P):
        C = int(input())
        bus_stop.append(lst[C])     # C에 해당하는 개수 갖고 오기

    print(f"#{tc}", *bus_stop)
