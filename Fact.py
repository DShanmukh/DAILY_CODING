def Fact(n):
  if n<=1:
    return 1
  return n*Fact(n-1)
n=int(input())
print(Fact(n))
  