n = int(input())
visited = [False]*n+1 #생각하기 쉽게 visited 0을 없다고 치고 1부터 저장함
answer = []

def print_answer():
    for elem in answer :
        print(elem, end = " ")
    print()

def choose(curr_num):
    if curr_num == n+1:
        print_answer()
        return
    
    for i in range(i,n+1):
        if visited[i] == False :
            continue
        visited[i] = True
        answer.append(i)

        choose(curr_num+1)

        answer.pop()
        visited[i] = False