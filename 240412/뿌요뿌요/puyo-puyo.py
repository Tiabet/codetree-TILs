n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y) :
        return False
    if visited[x][y] == True :
        return False
    return True

dxs, dys = [0,0,1,-1], [1,-1,0,0]

count = 0

def dfs(x,y):
    global count
    visited[x][y] = True
    count+=1
    for dx,dy in zip(dxs,dys):
        new_x = x+dx
        new_y = y+dy
        if can_go(new_x,new_y) and graph[new_x][new_y] == graph[x][y]:  
            dfs(new_x,new_y)
            
    
result = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == False :
            dfs(i,j)
            result.append(count)
            count=0


bomb = 0
for cnt in result :
    if cnt>=4:
        bomb+=1
print(bomb, max(result))