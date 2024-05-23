n, t = map(int, input().split())

graph = []
for _ in range(3):
    graph.extend(list(map(int, input().split())))
# print(graph)

for _ in range(t):
    tmp = []
    tmp.append(graph[-1])
    tmp.extend(graph[:-1])
    graph = tmp

#print(graph)
result = []
for i in range(3):
    result.append(graph[n*i:n*i+n])

# print(result)
for i in range(3):
    for j in range(n):
        print(result[i][j], end = " ")
    print()