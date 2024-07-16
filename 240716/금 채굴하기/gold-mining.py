n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def in_range(x,y):
    if 0<=x<n and 0<=y<n :
        return True
    else :
        return False
def get_num_of_gold(row, col, k):
    cnt = 0

    for i in range(n):
        for j in range(n):
            if abs(row-i) + abs(col-j) <= k:
                if graph[i][j] == 1:
                    cnt += 1

    return cnt

k=0
result = 0
while k<=n:
    gold_count = 0
    cost = 2*(k**2) + 2*k + 1
    for i in range(n):
        for j in range(n):
            cnt = get_num_of_gold(i,j,k)
            if cnt*m >= cost :
                gold_count = max(gold_count,cnt)

    result = max(gold_count,result)
    k+=1

print(result)