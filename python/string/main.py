s=input("enter the string : ")
def first(s):
    a=s.split()
    for i in a:
        print(i[0].upper()+".",end="")
    b=s.split()
    print()

def second(s):
    s=s.split()
    for i in range(len(s)):
        if(i==len(s)-1):
            print(s[i].capitalize())
        else:
            x=s[i]
            print(x[0].upper(),end=".")
    print()
            
def third(s):
    s=s.split()
    for i in s:
        print(i[::-1],end=" ")
    print()
    
def fourth(s):
    print(s.title())
    print()

def fivth(s):
    s=s.split()
    for i in range(len(s)):
        x=s[i]
        for j in  range(len(x)):
            if(j==0 or j==len(x)-1):
                print(x[j].upper(),end="")
            else:
                print(x[j],end="")
        print(end=" ")
    print()
    
first(s)
second(s)
third(s)
fourth(s)
fivth(s)