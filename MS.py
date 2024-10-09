n=int(input())
a=list(map(int,input().split()))
k=int(input())
l=[]
s=0
for i in range(len(a)-1):
  s=0
  s=a[i]+a[i+1]
  l.append(s)
print(max(l))
    