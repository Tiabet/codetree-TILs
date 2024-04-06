n = int(input())

for i in range(1,n+1):
    for j in range(0,n):
        if j!=n-1:
            print(i*(2**j), end = " ")
        else :
            print(i*(2**j))