m,n= map(int,input().split())

for i in range(m,n+1):    
    ch=True    

    for j in range(2,int(i**0.5)+1):   #2부터 i의 제곱근만 검사     
        if i%j==0:
            ch=False
            break
    if i==1:
        ch=False
        
    if ch:
        print(i)
