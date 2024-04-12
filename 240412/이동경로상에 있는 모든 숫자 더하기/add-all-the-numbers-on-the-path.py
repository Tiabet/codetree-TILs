N,T = map(int, input().split())

orders = input()

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

position = [(-1,0),(0,1),(1,0),(0,-1)]

def turn_position(idx,order):
    if order == 'R' :
        if idx + 1 < len(position):
            idx+=1
        else :
            idx=0
    else :
        if idx - 1 < 0:
            idx=len(position)-1
        else :
            idx-=1
    

    return idx

idx=0
result=0
row,col = N//2,N//2
result+=graph[row][col]

for i in range(T):
    order = orders[i]
    if order == 'F':
        if 0<=row+position[idx][0]<N and 0<=col+position[idx][1]<N:
            row+=position[idx][0]
            col+=position[idx][1]
            result+=graph[row][col]
    else : 
        idx = turn_position(idx,order)

print(result)