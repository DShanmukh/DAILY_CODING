n,m,k=map(int,input().split())
c=0
for i in range(n,m-1):
  r=i%10
  if r == k:
    c+=1
print(c) 