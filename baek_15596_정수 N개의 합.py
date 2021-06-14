#백준 15596 정수 N개의 합


a=[]
i=0
n= int(input("n값을 입력하세요: "))
while i<n:
    a.append(int(input("배열값을 입력: ")))
    i+=1


def solve (list):
    ans=0
    for i in a :
        ans+=i
    
    return ans

print(solve(a))
