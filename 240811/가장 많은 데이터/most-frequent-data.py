n = int(input())

dic = {}

for _ in range(1,n+1):
    st = input()
    if st not in dic :
        dic[st] = 1
    else :
        dic[st] += 1

max_value = 0
max_index = ""

for st in dic :
    if dic[st] > max_value :
        max_index = st
        max_value = dic[st]

print(max_value)