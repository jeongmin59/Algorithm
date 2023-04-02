# 5185_이진수
'''
- 16진수 1자리는 2진수 4자리로 표시됨
- N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램
- 2진수의 앞자리 0도 반드시 출력해야 함
'''

T = int(input())
for tc in range(1, T + 1):
    N, hex_str = input().split()
    N = int(N)
    ans = ''
    for h in hex_str:   # 16진수 각 자리 -> 10진수로
        if ord(h) >= ord('A'):  # A = 65
            h = ord(h) - ord('A') + 10  # 10~15
        else:
            h = int(h)  # 0~9

        tmp = ''    # 각 자리 2진수

        while h > 0:
            tmp = str(h % 2) + tmp  # 나머지
            h //= 2 # 몫은 나누기
        if len(tmp) <= 4:   # 16진수 1자리 <> 2진수 4자리
            tmp = '0' * (4-len(tmp)) + tmp
        ans += tmp

    print(f'#{tc} {ans}')
