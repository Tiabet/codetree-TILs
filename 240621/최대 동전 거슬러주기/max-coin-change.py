import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())

coins = list(map(int, input().split()))

dp = [0] * (m+1)
for i in range(1,m+1):
    dp[i] = -1

for i in range(1,m+1):
    for j in coins:
        if i-j>=0:
            if dp[i-j] == -1:
                continue
            dp[i] = max(dp[i],dp[i-j]+1)

# print(dp)
print(dp[m])