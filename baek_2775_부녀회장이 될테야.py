a=int(input())

for i in range(0,a):
    k=int(input())
    n=int(input())
    
    people=[i for i in range(1,n+1)] #0층리스트
    for i in range(k):  #층수만큼 반복
        for m in range(1,n):
            people[m]+=people[m-1]   #층별 각 호실의 사람수를 변경
    print(people[n-1]) #가장 마지막 수 출력
