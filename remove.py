n = int(input())
for i in range(n):
    n = int(input())
    l = list(map(int,input().split()))
    k = l[0]
    A = 0
    B = 0
    if k % 2 == 0:
        B += 1
    else:
        A += 1
    for i in range(1,n):
        if l[0] % 2 == 0:
            if  l[i] % 2 == 0:
              B += 1
            else:
              A += 1
        elif l[0] % 2 != 0:
          if  l[i] % 2 == 0:
            A += 1
          else:
            B += 1 
    if  A > B:
      print("Alice")
    else:
      print("Bob") 