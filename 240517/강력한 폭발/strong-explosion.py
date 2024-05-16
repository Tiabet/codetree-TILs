from itertools import product

# 폭탄의 종류에 따른 영향 영역
BOMB_TYPES = [
    [(0,0), (0,1), (0,-1), (1,0), (-1,0)], # 십자형
    [(0,0), (1,1), (1,-1), (-1,1), (-1,-1)], # 사각형
    [(0,0), (1,0), (2,0), (-1,0), (-2,0)]]

def in_bounds(x, y, n):
    return 0 <= x < n and 0 <= y < n

def calculate_destruction(board, bomb_positions, bomb_types, n):
    destroyed = set()
    for (x, y), bomb_type in zip(bomb_positions, bomb_types):
        for dx, dy in BOMB_TYPES[bomb_type]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny, n):
                destroyed.add((nx, ny))
    return len(destroyed)

def max_destruction(board, bomb_positions, n):
    max_destroyed = 0
    bomb_positions_list = list(bomb_positions)
    for bomb_types in product(range(len(BOMB_TYPES)), repeat=len(bomb_positions)):
        destroyed_count = calculate_destruction(board, bomb_positions_list, bomb_types, n)
        max_destroyed = max(max_destroyed, destroyed_count)
    return max_destroyed


n = int(input())
board = []
bomb_positions = set()
    
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(n):
        if row[j] == 1:
            bomb_positions.add((i, j))
    
result = max_destruction(board, bomb_positions, n)
print(result)