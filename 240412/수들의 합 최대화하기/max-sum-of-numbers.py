n = int(input())

nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

answer = []
visited = [False] * (n+1)

result = 0
tmp = 0
def choose(idx,count):

    global tmp, result
    if count==4 :
        result = max(result,tmp)
        return
    arr = nums[idx]
    

    for i in range(3):
        if visited[i] == True :
            continue 

        visited[i] = True
        
        tmp+=arr[i]
        choose(idx+1,count+1)

        visited[i] = False
        tmp -= arr[i]

choose(0,1)

print(result)