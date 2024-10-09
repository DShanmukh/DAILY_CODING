pos = -1
def Binary_search(l,k):
  low = 0
  up = len(l)-1
  while low <= up:
    mid =  (low+up)//2
    if l[mid] == k:
      globals()['pos'] = mid
      return True
    else:
      if l[mid] < k:
        low = mid+1
      else:
        up = mid-1
  return False     
l = list(map(int,input().split()))
k =int(input())
if Binary_search(l,k):
  print("Found",pos)
else:
  print("NOT Found")