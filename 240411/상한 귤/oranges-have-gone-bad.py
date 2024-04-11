n, m = tuple(map(int, input().split()))

rots = []

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            rots.append((i, j))

visited = [
    [0] * n
    for _ in range(n)
]

dist = [
    [0] * n
    for _ in range(n)
]

dxs, dys = [1,-1,0,0],[0,0,1,-1]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if inRange(nx, ny) and not visited[nx][ny] and a[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
 

from collections import deque

q = deque()
for x, y in rots:
    q.append((x, y))
    visited[x][y] = False

bfs()

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            dist[i][j] = -1
        elif a[i][j] == 2:
            dist[i][j] = 0
        elif a[i][j] == 1 and dist[i][j] == 0:
            dist[i][j] = -2

for i in range(n):
    print(*dist[i])