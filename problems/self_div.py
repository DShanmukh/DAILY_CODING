import math
start,end = map(int,input().split())
l = []
for i in range(start,end+1):
  c = 0
  o = i
  k = int(math.log10(i)+1)
  print(k)
  if o % 10 == 0:
    continue
  else:
    while o :
      r = o % 10
      if r == 0:
        continue
      elif i % r == 0:
        c += 1
      o = o //10 
      print(c)
  if c == k:
    l.append(i)
print(l)