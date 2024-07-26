n = int(input())

dp = [0 for _ in range(n)]

dp[0] = 9

for i in range(1,n):
    dp[i] = dp[i-1]*2 - i


print(dp[n-1]%(1000000000+7))