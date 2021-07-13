# 백준 1193 분수찾기
n=int(input())
i=1
j=2
num=1

if n==1:
    print("1/1")
    
while n>i:
    i+=j
    j+=1
    num+=1
    if n<i:
        if num%2==1:
            print("{}/{}".format(1-(n-i),num+(n-i)))
        else:
            print("{}/{}".format(num+(n-i),1-(n-i)))
            
    if n==i:
        if num%2==1:
            print("1/{}".format(num))
        else:
            print("{}/1".format(num))
        
    
