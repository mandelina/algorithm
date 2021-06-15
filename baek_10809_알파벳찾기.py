#백준 10809 알파벳찾기

s=str(input())
a=[]
for i in str(s):
    a.append(i)

for i in range (97,123):
    

    if chr(i) not in a:
        print(-1,end=" ")
    else:
        print(a.index(chr(i)),end=" ")
    
