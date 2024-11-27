#wap to accept 2 array and and calculate median of both 
l1=[1,2,4,3,5,6,7]
l2=[7,45,3,57,6]
l3=[]
l3=l1+l2
l3.sort()
n=len(l3)
if(n%2==0):
    r=(l3[n//2]+l3[n//2-1])/2
else:
    r=l3[n//2]
print(l3)
print(r)