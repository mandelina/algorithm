#백준 2581 소수

m= int(input())
n= int(input())
b=[]

for i in range(m,n+1):
    ch=True
    
    for j in range(2,i):
        if i%j==0:
            ch=False
            break
        
        if i==1:          # 1이 소수가 아닌것을 확인해주어야함..
            ch=False
            
    if ch==True:
        b.append(i)
        
if len(b)>0:
    print(sum(b))
    print(b[0])
    
else: print('-1')

