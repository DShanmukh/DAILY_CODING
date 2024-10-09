def height(l,n):
  s=0
  for i in range(1,len(l)):
    if(l[i]>=l[0]):
      continue
    else:
      s=s+(l[0]-l[i])
  return s
      
n=int(input())
l=list(map(int,input().split()))
print(height(l,n))