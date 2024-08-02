n = int(input())

dic = dict()

for _ in range(n):
    order = input().split()
    if order[0] == 'add':
        dic[int(order[1])] = int(order[2])

    elif order[0] == 'find' :
        if int(order[1]) in dic :
            print(dic[int(order[1])])
        else :
            print('None')

    elif order[0] == 'remove':
        dic.pop(int(order[1]))