n,m = map(int, input().split())
answer = []
lst = [i for i in range(1,n+1)]

def print_answer():
    for elem in answer :
        print(elem, end = " ")

    print()

def choose(cnt):
    if cnt == m+1:
        print_answer()
        
    
    # print(cnt,'실행')

    for num in lst:
        if cnt>1 and num>answer[-1]:
            answer.append(num)
            choose(cnt+1)
            answer.pop()

        elif cnt == 1:
            answer.append(num)
            choose(cnt+1)
            answer.pop()


    return

choose(1)