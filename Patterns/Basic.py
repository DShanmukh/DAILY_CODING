n = int(input())
# for i in range(n):
#   for j in range(i+1):
#     print("*",end=" ")
#   print()
# * 
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,n+1):
#   for j in range(i):
#     print(i,end=" ")
#   print("")
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(n,0,-1):
#   for j in range(i):
#     print(i,end=" ")
#   print("")
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(j,end=" ")
#   print("")
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range(1,n+1):
#   num = 1 
#   for j in range(n,0,-1):
#     if j > i :
#       print(" ",end=" ")
#     else:
#       print(num,end=" ")
#       num += 1
#   print("")
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# for i in range(1,n+1):
#   for j in range(i,0,-1):
#     print(j,end=" ")
#   print(" ")
# 1  
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
