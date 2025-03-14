n = int(input())
m = int(input())
l = [[int(input())for j in range(m)]for i in range(n)]
l1 = []  
for j in range(m):
  for i in range(n):
    print(l[j][0],end=" ")
  print()