n, m = map(int, input().split())

dic = {}

for i in range(1,n+1):
    value = input()
    dic[str(i)] = value
    dic[value] = i

for _ in range(m):
    to_find = input()
    print(dic[to_find])