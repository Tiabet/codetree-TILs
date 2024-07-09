n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0

for i in range(n):
    tmp = graph[i]
    idx = 0
    count=0
    temp=0
    while idx < n-1 :
        if tmp[idx] == tmp[idx+1]:
            # print('첫번째',i)
            temp+=1
            if temp>count:
                count=temp
        else:
            temp=0

        idx+=1
    if count >= m-1:
        result+=1

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(graph[j][i])
    
    idx = 0
    count=0
    temp=0
    while idx < n-1 :
        if tmp[idx] == tmp[idx+1] and:
            # print('첫번째',i)
            temp+=1
            if temp>count:
                count=temp
        else:
            temp=0

        idx+=1
    if count >= m-1:
        result+=1

print(result)