# 8320_직사각형을 만드는 방법
'''
- 변의 길이가 1인 정사각형 n개를 가지고 있음
- 정사각형을 이용해서 만들 수 있는 직사각형의 개수는 총 몇 개인지 출력
- input이 6일 때, output이 8임 >>> 2를 제외한 짝수 숫자면 사각형을 2개씩 만들 수 있음

'''

N = int(input())

ans = 0
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if i * j <= N:
            ans += 1
        else:
            break
print(ans)
