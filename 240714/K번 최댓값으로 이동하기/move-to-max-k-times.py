from collections import deque

n,k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

r,c = map(int, input().split())
r-=1
c-=1

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def can_go(new_x,new_y):
    if in_range(new_x,new_y) and graph[r][c]>=graph[new_x][new_y]:
        return True
    return False

dxs, dys = [0,0,-1,1],[1,-1,0,0]

total_visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(x,y):
    queue = deque()
    visited = [row[:] for row in total_visited] 
    queue.append((x,y))
    visited[x][y] = True
    total_visited[x][y] = True
    max_value = 0
    
    while queue:
        
        x,y = queue.pop()

        for dx,dy in zip(dxs,dys):
            new_x,new_y = x+dx,y+dy
            if can_go(new_x,new_y) and visited[new_x][new_y] == False:
                queue.append((new_x,new_y))
                # print("실행")
                max_value = max(max_value,graph[new_x][new_y])
                # print(max_value)
                visited[new_x][new_y] = True
    
    # print(max_value)
    result_x,result_y = 101,101

    found = False

    for i in range(n):
        for j in range(n):
            if graph[i][j] == max_value:
                found = True
                result_x,result_y = i,j
                break
        if found:
            break
    if (result_x, result_y)>(100,100):
        return (r,c)
    else :
        return (result_x,result_y)

for _ in range(k):
    r,c = bfs(r,c)

print(r+1,c+1)