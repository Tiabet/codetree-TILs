L = 0
L, Q = map(int, input().split())

Sushi_table = []
customer_table = [[None,0] for _ in range(L)]

t = 0

def eat(Sushi_table, customer_table):
    # Use a list comprehension to build a new list excluding the eaten sushi
    new_Sushi_table = []
    for j in range(len(Sushi_table)):
        sushi_eaten = False
        for i in range(L):
            if customer_table[i][0] == Sushi_table[j][0] and customer_table[i][0] is not None:
                if i == Sushi_table[j][1]:
                    customer_table[i][1] -= 1
                    sushi_eaten = True
                    break
        if not sushi_eaten:
            new_Sushi_table.append(Sushi_table[j])

    return new_Sushi_table, customer_table

def turn_table(Sushi_table, turn):
    for j in range(len(Sushi_table)):
        Sushi_table[j][1] = (Sushi_table[j][1] + turn)%L

    return Sushi_table


for _ in range(Q):
    inputs = list(map(str, input().split()))
    
    if int(inputs[0]) == 100 :
        Time,x,name = int(inputs[1]), int(inputs[2]), inputs[3]

        #테이블 돌아가면서 초밥 올려놓고 초밥 먹기
        while t<Time :
            Sushi_table = turn_table(Sushi_table, 1)
            Sushi_table.append([name,x])
            Sushi_table, customer_table = eat(Sushi_table, customer_table)
            t+=1
        
        #다먹은 손님 퇴장
        for i in range(L):
            if customer_table[i][1] == 0 and customer_table[i][0] != None :
                customer_table[i] = (None,0)

        #print(Sushi_table)
        #print(customer_table)

    elif int(inputs[0]) == 200:
        Time, x, name, n = int(inputs[1]), int(inputs[2]), inputs[3], int(inputs[4])

        #테이블 돌아가면서 손님 앉히고 초밥 먹기
        while t<Time :
            Sushi_table = turn_table(Sushi_table, 1)
            customer_table[x] = [name,n]
            Sushi_table, customer_table = eat(Sushi_table, customer_table)
            t+=1

        #다먹은 손님 퇴장
        for i in range(L):
            if customer_table[i][1] == 0 and customer_table[i][0] != None :
                customer_table[i] = [None,0]
        #print(Sushi_table)
        #print(customer_table)

    elif int(inputs[0]) == 300 :
        Time = int(inputs[1])

        #테이블 돌아가면서 초밥 먹기
        while t<Time :
            Sushi_table = turn_table(Sushi_table, 1)
            Sushi_table, customer_table = eat(Sushi_table, customer_table)
            t+=1

        #다먹은 손님 퇴장
        for i in range(L):
            if customer_table[i][1] == 0 and customer_table[i][0] != None :
                customer_table[i] = [None,0]
        
        num_customer = 0
        num_sushi = 0

        for i in range(L):
            if customer_table[i][0] != None :
                num_customer+=1
        
        for j in range(len(Sushi_table)):
            if Sushi_table[j][0] != None :
                num_sushi+=1
        #print(Sushi_table)
        #print(customer_table)
        print(num_customer, num_sushi)