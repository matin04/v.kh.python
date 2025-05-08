# while 4. /////////////////////

n=int(input())
k=int(input())
c=1
i=0
while i<k:
    c*=(n-1)
    c//=(i+1)
    i+=1
print(c)