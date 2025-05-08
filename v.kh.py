# for 4. /////////////////////


n=int(input())
k=int(input())
s=1
for i in range(1,k+1):
         s*=(n-i+1)
         s//=i
print(s)











