n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dxs, dys = [0,0,1,-1], [1,-1,0,0]

visited = [[0 for _ in range(n)] for _ in range(n)]

answer = [[-2 for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] != 0 or graph[x][y] !=1:
        return False
    return True

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 :
            answer[i][j] = -1

queue = []
def bfs(x,y):
    count = 1

    queue.append((x,y))
    answer[x][y] = 0
    visited[x][y] = 1
    
    while queue:

        x,y = queue.pop(0)

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy

            if can_go(new_x, new_y):
                queue.append((new_x,new_y))
                answer[new_x][new_y] = count
                visited[new_x][new_y] = 1
        count+=1
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2 :
            bfs(i,j)

for i in range(n):
    for j in range(n):
        print(answer[i][j], end = " ")
    print()