n,m,k = map(int, input().split())

#m은 크기, k는 위치

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#들어갈 위치 찾기
row = 0
to_stop = False
for i in range(1,n):
    for j in range(k-1,k+m-1):
        if graph[i][j] != 0 :
            row = i-1
            to_stop = True
            break
    if to_stop :
        break

for i in range(k-1,k+m-1):
    graph[row][i] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
    print()