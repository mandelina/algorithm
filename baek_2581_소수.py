#백준 2581 소수

m= int(input())
n= int(input())
b=[]

for i in range(m,n+1):
    ch=True
    for j in range(2,i):
        if i%j==0:
            ch=False
    if ch:
        b.append(i)
        
if len(b)>0:
    print(sum(b))
    print(min(b))
    print(b)
else: print(-1)

