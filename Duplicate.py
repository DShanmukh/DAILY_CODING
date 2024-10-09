l = list(map(int,input().split()))
arr = []
for i in range(len(l)):
  if l[i] != 0:
    arr.append(l[i])
  if l[i] == 0:
    c = i+1
    arr.insert(i+1,0)
print(arr)