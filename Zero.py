n=int(input())
l=list(map(int,input().split()))
i=0
j=len(l)-1
while i<j:
  if l[i] == 0:
    l[i],l[j]=l[j],l[i]
    j-=1
  else:
    i+=1
print(*l)
  