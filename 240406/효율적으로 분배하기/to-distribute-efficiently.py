n = int(input())

ar = n//5
arr = []
for i in range(ar+1):
    arr.append(i)

result = []
for i in range(len(arr)):
    if (n-arr[i]*5)%3==0:
        val = arr[i]+(n-arr[i]*5)//3
        result.append(val)

if result == [] :
    print(-1)
else :
    print(min(result))