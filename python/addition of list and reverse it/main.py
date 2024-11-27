l1=[2,4,3]
l2=[5,6,4]
l3=[]
s=""
s1=""
for i in l1:
    s=s+str(i)
for i in l2:
    s1=s1+str(i)
x=int(s[::-1])+int(s1[::-1])
while x>0:
    l3.append(x%10)
    x=x//10
print(l3)