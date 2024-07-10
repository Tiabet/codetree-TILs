k, n  = map(int, input().split())

lst = [i+1 for i in range(k)]

answer = []

def print_answer():
    same_count=0
    first_value = answer[-1]
    for elem in answer:
        if elem==first_value:
            same_count+=1
    if same_count == n and n>=2:
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