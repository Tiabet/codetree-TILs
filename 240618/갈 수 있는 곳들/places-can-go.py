from collections import deque

n,k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

starts = []

dxs, dys = [0,0,1,-1], [1,-1,0,0]
for _ in range(k):
    starts.append(list(map(int, input().split())))

def in_range(x,y):
    if 0<=x<n and 0<=y<n and graph[x][y]!=1 :
        return True
    return False

def bfs(x,y):

    visited = [[False for _ in range(n)] for _ in range(n)]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for dx, dy in zip(dxs,dys):
            new_x = x+dx
            new_y = y+dy

            if in_range(new_x,new_y) and visited[new_x][new_y]==False:
                queue.append((new_x,new_y))
                visited[new_x][new_y] = True
                graph[new_x][new_y] = 2

for start in starts :
    x,y = start[0]-1,start[1]-1
    bfs(x,y)

count=0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2 :
            count+=1

print(count)