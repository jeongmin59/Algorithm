# 2851_슈퍼 마리오
'''
- 버섯을 먹으면 점수를 받음. 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.
- 단, 중간에 먹는 것을 중단하면 이후 버섯은 모두 먹을 수 없음
- 만약 100에 가까운 수가 2개라면 98, 102 마리오는 큰 값을 선택 한다.
'''

mushroom = [int(input()) for _ in range(10)]
cnt = ans = 0

while cnt <= 9:
    ans += mushroom[cnt]

    if ans == 100:
        break
    elif ans > 100:
        if ans - 100 <= 100 - (ans - mushroom[cnt]):
            break
        else:
            ans -= mushroom[cnt]
            break
    cnt += 1

print(ans)
