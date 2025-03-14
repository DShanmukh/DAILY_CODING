n=int(input())
l=sorted(list(map(int,input().split())))
c=0
for i in range(len(l)):
  for j in range(i,len(l)):
    for k in range(j,len(l)):
      if((l[i]**2)+(l[j]**2) == (l[k]**2)):
        c=1
if(c==1):
  print("true")
else:
  print("False")