n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

s1,e1 = map(int, input().split())
s2,e2 = map(int, input().split())

s1 -= 1
s2 -= 1
e1 -= 1
e2 -= 1

tmp = []
for i in range(s1,e1+1):
    arr[i] = 0

for i in range(n):
    if arr[i] != 0 :
        tmp.append(arr[i])

arr = tmp
tmp = []
for i in range(s2,e2+1):
    arr[i] = 0

for i in range(len(arr)):
    if arr[i] != 0 :
        tmp.append(arr[i])

arr = tmp

print(len(arr))
for i in range(len(arr)):
    print(arr[i])