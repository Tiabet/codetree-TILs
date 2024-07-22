n, m = map(int,input().split())

arr = [[-1 for _ in range(m)] for _ in range(n)]
for j in range(n):
    start, end, score = map(int, input().split())
    start-=1
    end-=1
    for i in range(start,end+1):
        arr[j][i] = score

dp = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    dp[i][0] = 0


for i in range(1,m):
    for j in range(n):
        for k in range(n):
            if arr[j][i]!=-1 and dp[k][i-1] != -1 and arr[k][i-1]!=-1:
                dp[j][i] = max(dp[j][i], abs(arr[j][i] - arr[k][i-1])+dp[k][i-1])

result = 0
for i in range(n):
    result = max(result, dp[i][m-1])

print(result)
# print(dp)