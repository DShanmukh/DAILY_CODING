# # n = int(input())
# # l = list(map(int,input().split()))
# # c = 0
# # if 0 <= n < len(l):
# #   while l[n] != 0 :
# #     for i in range(len(l)):
# #       if l[i] != 0:
# #         l[i] -= 1
# #         c += 1
# #       if l[n] == 0:
# #         break
# # print(c)
# n = int(input())
# l = list(map(int,input().split()))
# l.sort()
# if l[0] + l[1] <= n:
#   print(n - (l[0]+l[1]))
# else:
#   print(n)
n = list(map(int,input().split()))
for i in range(len(n)):
  print(n[i])