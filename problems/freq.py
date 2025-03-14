n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
d={}
max=0
for i in l:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
for i,j in d.items():
  if j >=k:
    if max< j:
      max=j
  l1.append(i)
print(l1)