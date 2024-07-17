n, t = map(int, input().split())

graph = []
for _ in range(2):
    graph.extend(list(map(int, input().split())))

temp = [graph[-1]]
graph = graph[:-1]
temp.extend(graph)

for idx, num in enumerate(temp):
    if idx==n-1:
        print(num)
    else :
        print(num, end = ' ')