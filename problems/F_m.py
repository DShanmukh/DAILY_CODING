n=int(input())
l=list(map(int,input().split()))
d={}
p=[]
for i in l:
  if i not in d.keys():
    d[i]=1
  else:
    d[i]+=1
  if d[i]>1:
    p.append(i)
if len(p)>0:
  print(*set(p))
else:
  print("-1")