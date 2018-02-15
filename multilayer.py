n=int(input("enter no. of inputs: "))
t=int(input("enter threshold: "))
a=[]
x=0
for i in range(n):
    arr=input("enter no. ")
    a.insert(i,arr)
    for j in range(n-1):
        b[i]=a[j]*a[j+1]
    x+=b[i]
if x>=t:
    out=1
else:
    out=0