# 백준 4673 셀프넘버

#set:순서없음 중복허용x

num1=set(range(1,10001))   
num2=set()   #답을 넣을 set

for i in range(1,10001):    #i=850
    for j in str(i):         #j="8"  "5"   "0"
        i+=int(j)           #850+8+5+0
    num2.add(i)

self_num= sorted(num1-num2)

for i in self_num:
    print(i)
