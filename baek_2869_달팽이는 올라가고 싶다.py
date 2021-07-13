#2869 달팽이는 올라가고 싶다

a,b,v=map(int,input().split())
k=(v-b)/(a-b)  #ak-b(k-1)>=v 식 정리
print(int(k) if k==int(k) else int(k)+1)  #k(날짜)가 소수점일경우 올림을 해야하므로
