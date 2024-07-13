n, m = map(int, input().split())

starts = []
ends = []

for _ in range(m):
    start, end = map(int, input().split())
    starts.append(start)
    ends.append(end)

graph = [[] for _ in range(n+1)]

for start, end in zip(starts,ends):
    graph[start].append(end)
    graph[end].append(start)
    
visited = [False for _ in range(n+1)]

def dfs(point):
    for cur_point in graph[point]:
        if not visited[cur_point]:
            visited[cur_point] = True
            dfs(cur_point)

visited[1] = True
dfs(1)
print(sum(visited)-1)