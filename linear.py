# l= list(map(int,input().split()))
# k =int(input())
# c = False
# for i in range(len(l)):
#   if l[i] == k:
#     c = True
# if c:
#   print("FOUND")
# else:
#   print("NOT FOUND")
def Linear_Search(l,k):
  for i in range(len(l)):
    if l[i] == k:
      return True
  return False 
l = list(map(int,input().split()))
k = int(input())
if Linear_Search(l,k):
  print("Found")
else:
  print("NOT FOUND")