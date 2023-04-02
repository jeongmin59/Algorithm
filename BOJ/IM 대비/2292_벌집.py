# 2292_벌집
'''
- 육각형으로 이루어진 벌집이 있고, 중앙의 방 1부터 시작함
- 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나서 가는지 구하기
- 벌집의 개수가 6의 배수로 증가하는 것을 알 수 있음
'''

N = int(input())

honeycomb = 1   # 벌집의 개수, 1부터 시작
cnt = 1

while N > honeycomb:
    honeycomb += 6 * cnt
    cnt += 1

print(cnt)
