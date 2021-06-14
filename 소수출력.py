

N=int(input())  #값을 받음 (문제에선 N=100)
n=0

print("1부터 100까지 소수 ".format(N), end=' ')

for i in range(2,N+1):   #반복문으로 돌림 (1은 소수가 아니니까 2부터 N까지)
    boolean = True       #일단 모든 값을 true로 (소수가 다 맞다고 가정)
    for k in range(2,i):
        if i%k==0:         #만약 자기자신의 값전에 이전값으로 나누어 떨어지면 소수 x

            boolean= False   #소수가 아니므로 false로 바꿔줌
            break                #멈춘다
    if boolean is True:            #위 시행을 반복했는데  true이면 소수 
        print(i,end=' ')       #출력 (end= ' '는 한칸씩 뛰어서 출력하는거 )
        n+=1                     #몇개인지 개수셀려고 


print("\n 1부터 {}까지 소수는 {}개이다.".format(N,n))
