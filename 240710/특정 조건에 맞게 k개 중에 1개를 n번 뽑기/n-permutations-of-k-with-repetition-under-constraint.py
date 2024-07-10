k, n  = map(int, input().split())

lst = [i+1 for i in range(k)]

answer = []

def print_answer():
    tmp=0
    value = answer[0]
    for elem in answer:
        if elem==value:
            tmp+=1
        else :
            value = elem
            tmp=0

    if tmp>=3:
        return
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(cur_num):
    if cur_num == n+1:
        print_answer()
        return
    
    for i in range(k):
        answer.append(lst[i])
        choose(cur_num+1)
        answer.pop()

choose(1)