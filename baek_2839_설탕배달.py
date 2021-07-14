#백준 2839 설탕배달

'''N=int(input())
n=N//5
if (N-n*5)%3==0:
    n1=(N-n*5)//3
    print(n+n1)
elif N%3==0:
    print(N//3)

else:
    print(-1)

->오류발생 
'''
N=int(input())
bag=0
while N>=0:
    if N%5==0:
        bag+=(N//5)
        print(bag)
        break
    N-=3
    bag+=1
    
else :     #while문으로 N값이 0이 될때까지 나누어떨어지지않는경우  
    print(-1)
