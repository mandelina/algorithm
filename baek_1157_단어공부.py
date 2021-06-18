word= str(input()).upper()
word_uni=list(set(word)) #중복제거
s1=[]

for i in word_uni:      #각 알파벳들에 대하여    
    f=word.count(i)     #입력받은 문자열의 개수를 f에 대입
    s1.append(f)        #f값을 새로운 배열 s1에 append(즉 s1에는 word_uni배열에 있는 알파벳 인덱스 자리와 대응된 알파벳 개수가 존재)



if  s1.count(max(s1))>1: #최빈값이 중복
    print("?")
else:
    max_index=s1.index(max(s1)) #최빈값의 인덱스를 max_index에 대입
    print(word_uni[max_index])  
    
