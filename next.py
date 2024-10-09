n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
  for j in range(i,len(l)):
    if(l[i]<l[j]):
      k.append(l[j])
      break
    else:
      k.append(-1)
print(k)