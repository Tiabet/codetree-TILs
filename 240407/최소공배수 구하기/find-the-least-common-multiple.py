n, m = map(int, input().split())

target = n*m

for i in range(1,target+1) :
    if i % n == 0 and i % m == 0 :
        print(i)

        break