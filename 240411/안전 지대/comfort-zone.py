N,M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

K = 0

def is_watered(K,graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] <=K :
                graph[i][j] = 0
    return graph

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y,graph):
    if not in_range(x,y):
        return False
    if visited[x][y] != 0 or graph[x][y] == 0 :
        return False
    return True

dxs, dys = [1,-1,0,0] , [0,0,1,-1]

def dfs(x,y,graph):
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y,graph) :
            visited[new_x][new_y] = 1

            dfs(new_x, new_y,graph)



result = []

while K<100:
    K+=1

    tmp_graph = [x[:] for x in graph]

    visited = [[0 for _ in range(M)] for _ in range(N)]

    tmp_graph = is_watered(K,tmp_graph)

    count=0

    for i in range(N):
        for j in range(M):
            if can_go(i,j,tmp_graph):
                visited[i][j] = 1
                
                dfs(i,j,tmp_graph)

                count+=1
    
    result.append((K,count))


result = sorted(result, key = lambda x : (x[1],-x[0]))

print(result[-1][0], result[-1][1])