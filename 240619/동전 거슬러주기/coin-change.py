import sys

INT_MAX = sys.maxsize

n,m = map(int, input().split())

dp = [0] * (m+1)
arr = list(map(int, input().split()))

for i in range(1,m+1):
    dp[i] = INT_MAX

for i in range(1,m+1):
    for j in range(n):
        if i >= arr[j]:
            if dp[i-arr[j]] == INT_MAX:
                continue
            
            dp[i] = min(dp[i], dp[i-arr[j]] + 1)

# print(dp)
result = dp[m]

if result == INT_MAX:
    result = -1

print(result)