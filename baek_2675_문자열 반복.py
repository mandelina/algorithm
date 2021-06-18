n=int(input())
for i in range(0,n):
    n,s=input().split()
    n=int(n)
    for j in range(0,len(s)):
        print(n*s[j],end="")
    print(end="\n")
