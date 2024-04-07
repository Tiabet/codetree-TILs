n = int(input())

lst = list(map(int, input().split()))

def gcd(a,lst):
    if a<len(lst)-1:
        mini = 0
        for i in range(1,min(lst[a],lst[a+1])+1):
            if lst[a]%i == 0 and lst[a+1]%i==0:
                mini = i

        lst[a+1] = lst[a]*lst[a+1]//mini
        return gcd(a+1,lst)
    elif a == len(lst)-1 :
        return lst[-1]


print(gcd(0,lst))