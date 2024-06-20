import sys

n,m = map(int, input().split())

INT_MAX = sys.maxsize

arr = list(map(int, input().split()))

dp = [0] * (sum(arr)+1)
for i in range(1,sum(arr)+1):
    dp[i] = INT_MAX

for i in range(n):
    for j in range(sum(arr),-1,-1):
        if j >=arr[i]:
            if dp[j - arr[i]] == INT_MAX:
                continue
        dp[j] = min(dp[j],dp[j-arr[i]]+1)

answer = dp[m]
if answer == INT_MAX:
    answer = -1
print(answer)