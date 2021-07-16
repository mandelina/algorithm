# 1978 소수찾기
def prime(num):
    
    if num<=1 :
        return False
    
    for i in range(2,num):
        if num%i==0:
            return False
    return True

n=int(input())
a=[int(x) for x in input().split()]
count=0
for i in a:
    if prime(i):
        count+=1
print(count)
