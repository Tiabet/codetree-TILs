n = int(input())
visited = [False for _ in range(n+1)]

def print_answer(result):
    
    for elem in result :
        print(elem, end = " ")

    print()

answer = []

def simulate(cur_num):
    if cur_num == n+1 :
        print_answer(answer)
        return

    for i in range(n,0,-1):
        if visited[i] == False:
            answer.append(i)
            visited[i] = True
            simulate(cur_num+1)

            answer.pop()
            visited[i] = False


simulate(1)