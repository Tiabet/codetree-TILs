n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

r,c = map(int, input().split())
r-=1
c-=1

bomb_size = graph[r][c]-1

for i in range(r-bomb_size,r+bomb_size+1):
    if i in range(n):
        graph[i][c] = 0

for j in range(c-bomb_size,c+bomb_size+1):
    if j in range(n):
        graph[r][j] = 0

result = []
for col in range(n):
    tmp = []
    for i in range(n-1,-1,-1):
        if graph[i][col] !=0:
            tmp.append(graph[i][col])
            # print(i,col,"0아님")
    # print(tmp)

    while len(tmp) != n:
        tmp.append(0)
    result.append(tmp)

for j in range(n-1,-1,-1):
    for i in range(n):
        print(result[i][j], end = " ")
    print()