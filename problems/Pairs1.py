l=list(map(int,input().split()))
l1=list(map(int,input().split()))
k=int(input())
s=0
p=[]
for i in range(len(l)):
  for j in range(len(l1)):
    if(l[i]+l1[j]==k):
      print(l[i],l1[j],end="\n")