n=int(input())
l=list(map(int,input().split()))
for i in range (n):
  p=1
  for j in range(n):
    if i!=j:
      p=p*l[j]
  print(p)