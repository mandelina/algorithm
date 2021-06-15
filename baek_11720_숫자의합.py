#백준 11720 숫자의 합
n=int(input(""))
num=input("")
sum=0
for j in str(num):  #숫자를 문자열로 바꾸고
    sum+=int(j)     #각 자리수마다 더해준다
print(sum)
