# 3052_나머지

lst = []

for _ in range(10):
    num = int(input())
    lst.append(num % 42)

ans = []
for i in lst:
    if i in ans:
        pass
    else:
        ans.append(i)

print(len(ans))

