# 15230_알파벳공부
'''
abcdefghijklmnopqrstuvwxyz
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

T = int(input())
for tc in range(1, T + 1):
    lst = input()

    i = 0
    cnt = 0
    for j in range(len(lst)):
        if alphabet[i] == lst[j]:
            cnt += 1
            i += 1
        else:
            break

    print(f"#{tc} {cnt}")
