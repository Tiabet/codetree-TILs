n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#dxs,dys = [1,1,1,0,0,-1-1-1], [-1,0,1,-1,1,-1,0,1]
dxs, dys = [1, 1, 1, 0, 0, -1, -1, -1], [-1, 0, 1, -1, 1, -1, 0, 1]

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else :
        return False

def to_change(x,y):
    target_x, target_y = -1,-1
    value = 0
    for dx,dy in zip(dxs,dys):
        new_x,new_y = x+dx, y+dy
        if in_range(new_x,new_y) and graph[new_x][new_y]>value:
            target_x,target_y = new_x,new_y
            value = graph[new_x][new_y]
    #print(value)
    return target_x, target_y

def move_number(x,y,new_x,new_y):
    graph[x][y], graph[new_x][new_y] = graph[new_x][new_y], graph[x][y]


for _ in range(m):
    target = 1
    while True:
        to_stop = False
        if target == n**2+1:
            break
        for i in range(n):
            for j in range(n):
                if graph[i][j] == target :
                    new_i,new_j = to_change(i,j)
                    move_number(i,j,new_i,new_j)
                    to_stop = True
                    #print(f"{target} Finished")
                    break
            if to_stop:
                break
        target+=1
        

for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
    print()