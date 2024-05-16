k, n = map(int, input().split())

def comb(cur_num):
    if len(cur_num) == n :
        print(*cur_num)
        return
    
    for i in range(1,k+1):
        cur_num.append(i)
        comb(cur_num)
        cur_num.pop()
    

for i in range(1,k+1):
    comb([i])