n=int(input())
l=list(map(int,input().split()))
r=0
m=0
for i in l:
  k=l.count(i)
  if(k>1):
    r=i
for i in range(1,n+1):
  if i not in l:
    m=i
    break
print(r,m)