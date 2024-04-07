n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

max_cnt = 0
for i in range(0,n-2):
    for j in range(0,n-2):
        count=0
        for k in range(i,i+3):
            for l in range(j,j+3):
                if graph[k][l] == 1:
                    count+=1
        if count>max_cnt :
            max_cnt = count

print(max_cnt)