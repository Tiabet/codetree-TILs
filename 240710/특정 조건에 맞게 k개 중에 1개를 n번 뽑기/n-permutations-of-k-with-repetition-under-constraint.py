k, n  = map(int, input().split())

lst = [i+1 for i in range(k)]

answer = []

def print_answer():
    same_count=0
    tmp=0
    first_value = answer[0]
    for elem in answer:
        if elem==first_value:
            tmp+=1
        else :
            first_value = elem
            tmp=0
        same_count=max(same_count,tmp)

    if same_count>=2:
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