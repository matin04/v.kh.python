# while 7. /////////////////////

a=float(input())
b=float(input())
k=1
l=abs(b)
i=0
while i<l:
    k*=a
    i+=1
if(b<0):
   print(1/k)
else:
    print(k)