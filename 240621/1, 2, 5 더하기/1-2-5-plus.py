import sys

INT_MAX = sys.maxsize

n = int(input())

dp = [0] * (n+1)


dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = 9 

if n>5:
    for i in range(6,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-5]

print(dp[n]%10007)