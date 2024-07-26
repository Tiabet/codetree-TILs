n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0] = graph[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + graph[i][0]
    dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + graph[i][1]
    dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + graph[i][2]

print(max(dp[n-1]))