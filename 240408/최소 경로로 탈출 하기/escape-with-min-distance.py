from collections import deque

X,Y = map(int, input().split())

q = deque()
graph = []
for _ in range(X):
    graph.append(list(map(int, input().split())))

visited = [[False for i in range(Y)] for j in range(X)]

step = [[0 for i in range(Y)] for j in range(X)]

def in_range(x,y):
    return 0<=x and x<X and 0 <= y and y< Y

def push(x,y,s):
    step[x][y]=s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dxs = [1, -1, 0, 0]
    dys = [0, 0, -1, 1] #동서북남

    while q :
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy

            if in_range(new_x, new_y) and not visited[new_x][new_y]:
                if graph[new_x][new_y]==1:
                    push(new_x,new_y,step[x][y]+1)


push(0,0,0)
bfs()
if step[X-1][Y-1] == 0 :
    print(-1)
else :
    print(step[X-1][Y-1])