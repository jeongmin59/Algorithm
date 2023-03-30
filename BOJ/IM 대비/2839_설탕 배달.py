# 2839_설탕 배달

'''
- 설탕을 정확하게 Nkg 배달해야 함. 3kg, 5kg로 최대한 적은 봉지를 들고 가려고 함
- 배달하는 봉지의 최소 개수를 출력. 정확하게 만들 수 없다면 -1 출력

- 가장 큰 단위인 5만으로 나눠질 경우
- 최소한의 3과 최대한의 5를 사용한 조합으로 나눠질 경우
- 3으로 나눠질 경우
- 5와 3으로 나눠지지 않는 경우
'''

sugar = int(input())

if sugar % 5 == 0:
    print(sugar // 5)

else:
    cnt = 0
    while sugar > 0:
        sugar -= 3
        cnt += 1
        # 3과 5의 조합
        if sugar % 5 == 0:
            cnt += sugar // 5
            print(cnt)
            break
        # 나눠질 수 없는 경우
        elif sugar == 1 or sugar == 2:
            print(-1)
            break
        # 3으로만 나눠지는 경우
        elif sugar == 0:
            print(cnt)
            break
