l = list(map(int,input().split()))
for i in range(1,len(l)):
  for j in range(i-1,0,-1):
    if l [i] > l[j]:
      l[j],l[j+1] = l[j+1],l[j]
    else:    
      break
print(l)
      