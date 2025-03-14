def iso(n):
  d={}
  l=[]
  for i in n:
    if i not in d:
      d[i]=1
    else:
      d[i]+=1
    l.append(d[i])
  return l
n=input()
m=input()
k=[]
if(len(n)!=len(m)):
  print("0")
else:
  if(iso(n)==iso(m)):
    k.append(iso(n))
  print(k)  