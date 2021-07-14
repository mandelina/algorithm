'''
백준 10250 ACM호텔
층 = n번째손님 나누기 호텔의층수 한것의 나머지
호수 = n//h+1 (나누어 떨어지지 않을시)
     = h (나누어떨어지면 맨 위층)


'''
T=int(input())    #테스트데이터
for i in range(0,T):
    h,w,n=map(int,input().split())  # 호텔의층수,각층방수,몇번째손님
    if h>=n:
        print("{}01".format(n))
    elif h<n:
        num=n//h+1
        floor=n%h
        
        if n%h==0:
            num=n//h #나누어 떨어지므로
            floor=h  #꼭대기방

        print("{}".format(floor*100+num))
       
        


