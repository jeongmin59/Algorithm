# 2851_슈퍼 마리오
'''
- 버섯을 먹으면 점수를 받음. 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.
- 단, 중간에 먹는 것을 중단하면 이후 버섯은 모두 먹을 수 없음
- 만약 100에 가까운 수가 2개라면 98, 102 마리오는 큰 값을 선택 한다.
'''

mushroom = [int(input()) for _ in range(10)]
ans = 0

for i in range(len(mushroom)):
    ans += mushroom[i]
    if ans == 100:
        print(ans)
        break
    if ans > 100:
        cur = ans
        prev = ans - mushroom[i]
        if abs(100 - cur) < abs(100 - prev):
            print(cur)
            break
        elif abs(100 - cur) == abs(100 - prev):
            print(cur)
            break
        else:
            print(prev)
            break
print(ans)
