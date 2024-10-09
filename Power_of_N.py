import math
def Sq(n):
  c=0 
  for i in range(0,int(math.sqrt(n)+1)):
    if n == (2**i) :
      c=1
  if c == 0:
    return False
  else:
    return True 
n=int(input())
print(Sq(n))