dic = {'Bessie' : 0, 'Elsie' : 0 , 'Daisy' : 0 , 
'Gertie' : 0, 'Annabelle' : 0, 'Maggie' : 0, 'Henrietta' : 0}


n = int(input())
for i in range(n):
    student, score = map(str, input().split())
    score = int(score)

    dic[student]+=score

dic = sorted(dic.items(), key = lambda x : x[1])
lowest = dic[0][1]
printed = False
for i in range(len(dic)):
    if dic[i][1]>lowest and i<len(dic)-1 and dic[i+1][1] != dic[i][1] :
        print(dic[i][0])
        printed = True
        break

    elif dic[i][1] > lowest and (i<len(dic)-1 and dic[i+1][1] == dic[i][1]) :
        print("Tie")
        printed = True
        break
    elif i==len(dic)-1 and dic[i][1] > lowest :
        print(dic[i][0])
        printed = True
        break
    else :
        continue

if i == len(dic)-1 and printed == False:
    print("Tie")