#2292 백준 알고리즘
# 1 :1개
# 2~7(6) : 2개 / 8~19(12) :3개 /20~37(18) :4개 ... 

n=int(input())
cnt=1
cnt_6= 6
count=1

while n>cnt:
    count+=1
    cnt+=cnt_6
    cnt_6+=6
    
print(count)
