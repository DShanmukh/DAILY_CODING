def Binary(l,n):
  lo=0
  h=len(l)-1
  if( lo > h):
    return 0
  k= (lo+h)
  if l[k] > n:
    for i in range(lo,k-1):
      if l[i] == n:
        return 1
      else:
        return 0
  else:
    for i in range(k-1,h):
      if l[i] == n:
        return 1 
      else:
        return 0 
l=list(map(int,input().split()))
n=int(input())
print(Binary(l,n))