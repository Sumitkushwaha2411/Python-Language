n=int(input("enter the number :"))
sum=0
i=1
while(n>0):
    a=n%10
    if(a!=0):
        sum=sum+a*i
        i=i*10
    n=n//10
print(sum)
        