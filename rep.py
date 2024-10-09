d = {}
l = list(map(int,input().split()))
c = 0
for i in  range(len(l)):
  for j in range(i,len(l)):
    if l[i] == l[j]:
      c = i+1
      break
print(c)
