INT_MIN = -1000

n = int(input())
a = list(map(int, input().split()))

dp = [INT_MIN for _ in range(n)]
dp[0] = 1

for i in range(1,n):
    for j in range(0,i):
        if dp[j] == INT_MIN :
            continue
        
        if a[i] < a[j] :
            dp[i] = dp[j]+1
        else :
            dp[i] = max(1,dp[i])


print(max(dp))