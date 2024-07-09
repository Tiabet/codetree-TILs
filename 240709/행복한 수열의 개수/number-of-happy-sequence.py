# Read n and m
n, m = map(int, input().split())

# Read the graph (n x n matrix)
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0

# Function to check consecutive elements in a list
def count_consecutive(lst, m):
    idx = 0
    value = lst[0]
    count = 0
    while idx < len(lst) - 1:
        if lst[idx] == lst[idx + 1]:
            if count == 0:
                value = lst[idx + 1]
                count = 1
            else:
                if lst[idx] == value:
                    count += 1
        else:
            count = 0
            value = lst[idx + 1]
        if count >= m - 1:
            return True
        idx += 1
    return False

# Check rows
for i in range(n):
    if count_consecutive(graph[i], m):
        result += 1

# Check columns
for i in range(n):
    column = [graph[j][i] for j in range(n)]
    if count_consecutive(column, m):
        result += 1

# Print the result
print(result)