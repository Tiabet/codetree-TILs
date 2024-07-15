n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

max_num = 0

#누운3자
for i in range(n):
    for j in range(m-2):
        tmp = graph[i][j] + graph[i][j+1] + graph[i][j+2]
        max_num = max(tmp, max_num)

#선3자
for j in range(m):
    for i in range(n-2):
        tmp = graph[i][j] + graph[i+1][j] + graph[i+2][j]
        max_num = max(tmp, max_num)

for i in range(n-1):
    for j in range(m-1):
        tmp = graph[i][j] + graph[i+1][j] + graph[i][j+1]
        max_num = max(tmp, max_num)


for i in range(n-1):
    for j in range(m-1):
        tmp = graph[i][j] + graph[i+1][j+1] + graph[i][j+1]
        max_num = max(tmp, max_num)

for i in range(n-1):
    for j in range(m-1):
        tmp = graph[i][j] + graph[i+1][j] + graph[i+1][j+1]
        max_num = max(tmp, max_num)

for i in range(n-1):
    for j in range(m-1):
        tmp = graph[i+1][j] + graph[i+1][j+1] + graph[i][j+1]
        max_num = max(tmp, max_num)


print(max_num)