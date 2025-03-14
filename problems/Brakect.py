n=int(input())
a=0
b=1
for i in range(n+1):
  t=a+b
  if((i)==(n)):
    print(a)
  a=b
  b=t