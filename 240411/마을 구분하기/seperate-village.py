N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


visited = [[False for _ in range(N)] for _ in range(N)]

people_nums = []
people_num = 0

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == True or graph[x][y] == 0:
        return False
    return True

def dfs(x,y):
    global people_num

    dxs, dys = [1,-1,0,0] , [0,0,1,-1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x,new_y):
            visited[new_x][new_y] = True

            people_num +=1
            dfs(new_x,new_y)

for i in range(N):
    for j in range(N):
        if can_go(i,j):

            visited[i][j] = True
            people_num = 1

            dfs(i,j)

            people_nums.append(people_num)

people_nums.sort()

print(len(people_nums))
for num in people_nums:
    print(num)