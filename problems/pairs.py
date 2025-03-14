n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
k={}
for i in l:
  p=m-i
  if p in k:
    c+=k[p]
  if i in k:
    k[i]+=1
  else:
    k[i]=1
print(c)