n=input()
l=int(input())
p=[]
for i in n:
  p.append(i)
  while l!=0:
    r=l%10
    p.append(r)
    l=l//10
print(p)