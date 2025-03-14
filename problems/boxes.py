n = list(map(int,input().split()))
d = {}
s = 0
for i in n:
  if i not in d:
    d[i] = 1
  else:
    d[i] += 1
for j in d.values():
  s = s + (j*j)
print(s)