arr=list(map(int,input().split()))
c=0
l=[]
for i in range(len(arr)-1):
  if(arr[i-1]%2!=0):
    if(arr[i]%2!=0 and arr[i+1]%2!=0):
      c+=1
    else:
      c=0
      continue
if(c==1):
  print("true")
else:
  print("False")