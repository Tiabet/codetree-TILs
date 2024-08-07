n, m = map(int, input().split())

arr = list(map(int, input().split()))

dic = {}

for num in arr:
    if num not in dic :
        dic[num] = 1
    else :
        dic[num] += 1

to_print = list(map(int, input().split()))

answer = []
for i in to_print :
    if i in dic :
        answer.append(dic[i])
    else :
        answer.append(0)

print(*answer)