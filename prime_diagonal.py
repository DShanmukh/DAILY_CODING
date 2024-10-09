r = int(input())
c = int(input())
l1 = r
l = [[int(input())for j in range(c)]for i in range(r)]
for i in range(r):
  print(l[i][l1-i-1],l[i][i],end=' ')
  print()