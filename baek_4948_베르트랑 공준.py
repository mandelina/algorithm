#베르트랑 공준 4948

#에라토스테네스 체 이용

def prime_list(n):
    s=[True]*n          #n개 요소 true로 설정 (소수로 간주)
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i+i,n,i):  #i 이후 i 배수들을 false
                s[j]=False
                
    return [i for i in range(2,n) if s[i]==True]

while 1:
    n= int(input())
    if n==0:
        break
    li=prime_list(2*n+1)
    print(len([i for i in li if i>n]))
