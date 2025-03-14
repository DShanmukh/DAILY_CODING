n=int(input())
l=list(map(int,input().split()))
e=len(l)-1
for i in range(len(l)):
  for j in range(e,-1,-1):
    if(l[i]==0):
      l[j]=l[j-1]
print(l)