n=int(input())
l=list(map(int,input().split()))
k=l[-1]
c=[]
c.append(k)
for i in range(n-2,-1,-1):
  if(l[i]>=k):
    c.append(l[i])
    k=l[i]
c.reverse()
print(c)