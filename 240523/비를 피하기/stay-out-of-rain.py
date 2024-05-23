from collections import deque

n, h, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dxs, dys = [0,0,1,-1], [1,-1,0,0]

def in_range(x,y):
    if 0<=x<n and 0<=y<n :
        return True
    return False

def bfs(x,y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((x,y,0))
    visited[x][y] = True

    while queue:
        x,y,count = queue.popleft()
        for dx,dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if in_range(new_x,new_y) and visited[new_x][new_y] == False and graph[new_x][new_y] !=1:
                if graph[new_x][new_y] == 3:
                    return count+1
                else :
                    visited[new_x][new_y] = True
                    queue.append((new_x,new_y,count+1))
                
    return -1

arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2 :
            arr.append(bfs(i,j))

result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            result[i][j] = arr.pop(0)

for i in range(n):
    for j in range(n):
        print(result[i][j], end = " ")
    print()