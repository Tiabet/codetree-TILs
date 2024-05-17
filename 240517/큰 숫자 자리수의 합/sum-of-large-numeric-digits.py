num1, num2, num3 = map(int, input().split())

num = num1*num2*num3

result = 0

def cal(num):
    global result
    tmp, num = num%10, num//10
    result+=tmp

    if num>0:
        cal(num)

cal(num)
print(result)