from collections import deque

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    if 0<=x<n and 0<=y<m :
        return True
    else :
        return False

def can_go(x,y):
    if in_range(x,y) and visited[x][y] == False:
        return True
    else:
        return False

dxs, dys = [0,0,1,-1],[1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        x,y = queue.pop()
        for dx,dy in zip(dxs,dys):
            
            new_x,new_y = x+dx,y+dy
            if can_go(new_x,new_y):
                queue.append((new_x,new_y))
                visited[new_x][new_y] = True

bfs(0,0)
print(int(visited[n-1][m-1]))