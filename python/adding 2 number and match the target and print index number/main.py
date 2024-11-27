l=[53,5,7,2,9,8]
a=[]
t=0
target=int(input())
for i in range(0,len(l),1):
    for j in range(i+1,len(l),1):
        if((l[i]+l[j])==target):
            a.append(i)
            a.append(j)
            t=1
    if(t==1):
        break
print(a)

    
