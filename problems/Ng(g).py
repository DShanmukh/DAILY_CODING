n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
  for j in range(i+1,len(l)):
    if l[i]<l[j]:
      l1.append(l[j])
      break
    else:
      continue
print(l1)