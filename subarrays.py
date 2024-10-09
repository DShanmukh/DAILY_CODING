n = int(input())
l = list(map(int,input().split()))
s = 0
for i in range(len(l)):
  for j in range(i,len(l)):
    x = l[i:j+1]
    if len(x) % 2 != 0:
      print(x)
      s += sum(x)
print(s) 