#백준 2941 크로아티아 알파벳
a=input()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia:
    if i in a:
        a=a.replace(i," ") #알파벳을 하나의 공백으로 바꿔줌     
print(a)    
print(len(a))
            
