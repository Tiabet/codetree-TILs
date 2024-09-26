from sortedcontainers import SortedDict

sd = SortedDict()

n = int(input())

for _ in range(n):
    order = input().split()

    if order[0] == "add":
        sd[int(order[1])] = int(order[2])
    elif order[0] == 'remove' :
        sd.pop(int(order[1]))
    elif order[0] == 'find' :
        if int(order[1]) in sd :
            print(sd[int(order[1])])
        else :
            print("None")
    else :
        if len(sd) == 0:
            print("None")
        else :
            for key, value in sd.items():
                print(value, end = " ")
            print()