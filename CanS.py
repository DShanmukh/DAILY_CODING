n = int(input())
for i in range(n):
  m = int(input())
  l = list(map(int,input().split()))
  k = sum(l)
  c = 0
  for j in range(1,(k//2)+1):
    if j**2 == k:
      c = 1 
  if c == 1:
    print("Yes")
  else:
    print("No")