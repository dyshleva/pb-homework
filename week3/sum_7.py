max_nat = int(input())

ans = 0

for i in range(max_nat+1):
    if (i % 7) == 0:
        ans += i

print(ans)

