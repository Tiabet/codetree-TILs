a = input()
b = input()

idx=0
count=0

while idx<len(b)-1:
    locate = a.find(b[idx])
    if a[locate+1:].find(b[idx+1]) == -1 :
        idx+=1
        count+=1
    else :

        idx+=1

print(count+1)