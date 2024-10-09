l =list(map(int,input().split()))
n = len(l)
l1 = []
c = 0
for i in range(0, n  ,2):
  for j in range(i):
    l1.append(l[j])
print(l1)