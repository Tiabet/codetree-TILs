X,Y = map(int, input().split())

graph = []
for _ in range(X):
    graph.append(list(map(int,input().split())))

def in_range(x,y):
    return 0<=x and x<X and 0<=y and y<Y
answer = [[0 for _ in range(Y)] for _ in range(X)]
visited = [[0 for _ in range(Y)] for _ in range(X)]
order = 1

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    return True

def dfs(x,y):
    global order

    dxs,dys = [1,0] , [0,1] #아래, 오른쪽

    for dx, dy in zip(dxs, dys):
        new_x , new_y = x + dx, y + dy

        if can_go(new_x,new_y):
            answer[new_x][new_y] = order
            order+=1
            visited[new_x][new_y]=1
            dfs(new_x,new_y)


answer[0][0] = order
order+=1
visited[0][0] = 1
dfs(0,0)

if answer[X-1][Y-1] != 0 :
    print(1)
else :
    print(0)