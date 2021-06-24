# 백준 5622 다이얼

s= input("")
dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
t=0

for i in range(len(s)):
    for j in dial:
        if s[i] in j:
            t = t+ dial.index(j)+3
print(t)
