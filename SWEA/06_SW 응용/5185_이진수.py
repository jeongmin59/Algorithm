# 5185_이진수
'''
- 16진수 1자리는 2진수 4자리로 표시됨
- N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램
- 2진수의 앞자리 0도 반드시 출력해야 함
'''

T = int(input())
for tc in range(1, T + 1):
    N, hex_str = input().split()
    dec_str = int(hex_str, 16)  # 16진수 -> 10진수
    bin_str = bin(dec_str)[2:]  # 10진수 -> 2진수 (앞 문자열 0b제거)

    num = len(bin_str) % 4
    if num != 0:
        bin_str = '0' * (4 - num) + bin_str

    print(f"#{tc} {bin_str}")

