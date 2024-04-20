n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][0] = graph[i][0]

print(dp[n-1])