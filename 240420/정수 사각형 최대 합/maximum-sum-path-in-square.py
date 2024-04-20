n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = graph[0][0]

for i in range(1,n):
    dp[0][i] = dp[0][i-1] + graph[0][i]
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i-1][j]+graph[i][j], dp[i][j-1]+graph[i][j])
        

print(dp[n-1][n-1])