#백준 1065 한수

n=int(input(""))
def hansu(n):
    number=0
    for i in range(1,n+1):
        num_list=list(map(int,str(i)))  #str함수로 문자열로 변환 -> 각자릿수를 분리 후 int타입변환
        if i<100:
            number+=1
        elif num_list[0]-num_list[1]==num_list[1]-num_list[2]:
            number+=1
    return number
print(hansu(n))
