#1152 단어의개수
s=input("")

if s=="":         #" "으로 하면 오류남.. else로 넘어감
    print(0)
    
else:
    w=s.split(" ")
    while "" in w:       
        w.remove("")
print(len(w))
