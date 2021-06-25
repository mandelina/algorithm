#백준 1316 그룹 단어 체커
n=int(input())
num=0
for i in range(n):
    a=input()
    
    for j in range(len(a)):     
        if j!=len(a)-1:
            if a[j]==a[j+1]:
                pass
            elif a[j] in a[j+1:]:
                break
        else:
            num+=1

print(num)
