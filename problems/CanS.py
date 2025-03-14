# n = int(input())
# for i in range(n):
#   m = int(input())
#   l = list(map(int,input().split()))
#   k = sum(l)
#   c = 0
#   for j in range(1,(k//2)+1):
#     if j**2 == k:
#       c = 1 
#   if c == 1:
#     print("Yes")
#   else:
#     print("No")
# print(15*7/3 + 1)
# s = input()
# for i in range(len(s)):
#   if s[i].islower():
#     print(s[i].upper(),end="")
#   else:
#     print()
#     print(s[i].lower(),end="")
# while i<len(s):
#   if s[i].islower():
#     print(s[i].upper(),end="")
#   else:
#     print()
#     print(s[i].lower(),end="")
#   i += 1
# n = list(map(int,input().split()))
# od = 0
# ev = 0
# ev_i = 0
# for i in range(len(n)):
#   if i % 2 != 0:
#     od += n[i]
#   else:
#      ev ^=  n[i]
# print(od - ev)
# n = input()
# i = 0
# j = i + 1
# c = 1
# while j < len(n):
#   if n[i] == n[j]:
#     j += 1
#     c += 1
#   else:
#     print(n[i],c, end="")
#     i = j
#     j = i + 1
#     c = 1
# print(n[i],c, end="")
# d = {}
# l = []
# for i in n:
#   if i not in d:
#     d[i] = 1
#   else:
#     d[i] += 1
# for i,j in d.items():
#   l.append(i)
#   l.append(j)
# print("".join(map(str,l)))
# _____second max_____________
# n = list(map(int,input().split()))
# ma = max(n)
# l = []
# min = 0
# for i in range(len(n)):
#   if n[i] < ma:
#     l.append(n[i])
# print(max(l))
# n =list(map(int,input().split()))
# max_sum = n[0]
# current_sum = n[0]
# for i in range(1,len(n)):
#   current_sum = max(n[i],n[i] + current_sum)
#   if current_sum > max_sum:
#     max_sum = current_sum
# print(max_sum)
n = list(map(int,input().split()))
max_pair = 0
pro = 1
i = 0
j = 0
k2 = set(n) 
for i in range(len(n)):
  k = n[i]
  k1 = 18 - n[i]
  if k1 in k2:
    if k * k1 > max_pair:
      max_pair = k * k1
      o = max(k,k1)
      j = min(k,k1)
print(o,j)