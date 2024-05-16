n = int(input())

possible = ['1','22','333','4444']
nums = ''

answer = 0

def beautiful(nums):
    global answer
    if len(nums) == n :
        answer+=1
        return
    elif len(nums)>n:
        return

    for i in range(4):
        new_nums = nums+possible[i]
        beautiful(new_nums)
        
beautiful('')
print(answer)