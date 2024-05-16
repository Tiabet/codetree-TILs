n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0

bombs = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            bombs.append((i,j))

def bomb1(x,y):
    start = max(x-2,0)
    end = min(x+2,n-1)

    for j in range(start,end+1):
        visited[j][y] = True

def bomb2(x,y):
    x_start = max(x-1,0)
    x_end = min(x+1,n-1)
    y_start = max(y-1,0)
    y_end = min(y+1,n-1)

    for i in range(x_start,x_end+1):
        visited[i][y] = True
    for j in range(y_start,y_end+1):
        visited[x][j] = True

def bomb3(x,y):
    x_start = max(x-1,0) 
    x_end = min(x+1,n-1) 
    y_start = max(y-1,0) 
    y_end = min(y+1,n-1) 

    visited[x_start][y_start], visited[x_end][y_start], visited[x][y], visited[x_start][y_end], visited[x_end][y_end] = True, True, True, True, True

def bomb(cur_nums):
    global answer, visited
    if len(cur_nums) == len(bombs):
        visited = [[False for _ in range(n)] for _ in range(n)]
        cur_shot = 0
        for num in range(len(cur_nums)):
            i,j = bombs[num]
            if cur_nums[num] == 1 :
                bomb1(i,j)

            elif cur_nums[num] == 2:
               bomb2(i,j)

            elif cur_nums[num] == 3:
                bomb3(i,j)
                cur_shot-=2

        # cur_shot = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == True:
                    cur_shot+=1
        answer = max(answer,cur_shot)
        # print(cur_shot)
        #visited = [[False for _ in range(n)] for _ in range(n)]
        #print(answer)
        return 

    for i in range(1,4):
        cur_nums.append(i)
        bomb(cur_nums)
        cur_nums.pop()

bomb([])

print(answer)