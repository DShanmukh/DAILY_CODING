n=list(map(int,input().split()))
c=0
for i in range(0,len(n)):
  c=n.count(n[i])
  for j in range(i+1,len(n)):
    if(n[i]>=n[j]):
      n[i],n[j]=n[j],n[i]
  if(c==0):
    print(n[-3])
else:
  k=set(n)
  l=list(k)
  print(l[-3])