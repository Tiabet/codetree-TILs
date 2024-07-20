from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

comb = combinations(arr, m)

max_xor = 0

for c in comb:
    xor_value = c[0]
    for i in range(m) :
        if i!=0:
            xor_value = xor_value^c[i]
    if xor_value > max_xor:
        max_xor = xor_value

print(max_xor)