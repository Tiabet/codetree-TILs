n, r, c = map(int, input().split())

r-=1
c-=1

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else :
        return False

dxs, dys = [-1,1,0,0],[0,0,-1,1]

result = []
result.append(graph[r][c])
while True :
    start = graph[r][c]

    for dx,dy in zip(dxs,dys):
        new_r, new_c = r+dx, c+dy
        if in_range(new_r,new_c) and graph[new_r][new_c] > start:
            r,c = new_r, new_c
            break
    if graph[r][c] == result[-1] :
        break
    else :
        result.append(graph[r][c])

print(*result)