def Sort(arr):
  if len(arr) <= 1 :
    return True
  if(arr[0] <= arr[1]):
    return Sort(arr[1:])
  return False 
  
arr=list(map(int,input().split()))
print(Sort(arr))