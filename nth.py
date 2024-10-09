# ------>swapping two arrays
# l = list(map(int,input().split()))
# l1 = list(map(int,input().split()))
# for i in range(len(l)):
#   l[i],l1[i] = l1[i],l[i]
# print("list 1 is : ",l)
# print("list 2 is : ",l1)
# ------>sort the alphabets
# s = input()
# k = "".join(sorted(s))
# print(k)
# ---->panagram
# l = list(map(str,input().split()))
# t = [0]*26
# for i in range(len(l)):
#   for j in range(len(l[i])):
#     t[ord(l[i][j]) - ord('a')] = 1
# for k in range(len(t)):
#   o = 0
#   if t[k] == 0:
#     o = k+ord('a')
#     print(chr(o),end="")
# -----> sumof primes in given range
# def Is_prime(n):
#   if n <= 1:
#     return False
#   for i in range(2,int(n**0.5)+1):
#     if n % i == 0:
#       return False
#   return True
# n = int(input())
# s = 0
# for i in range(1,n+1):
#   if Is_prime(i):
#     s+=i
# print(s)
# ---------------------- Collatz sequence ----------------------------------------
# def Collatz(n):
#   c = 0
#   if n == 1:
#     return 
#   if n % 2 == 0:
#     return Collatz(n//2)
#   else:
#     return Collatz(3*n+1)
# n = int(input())
# print(Collatz(n))
# n = int(input())
# c = 0 
# while(n != 1):
#   if n % 2 == 0:
#     n = n // 2
#     c += 1
#   else:
#     n = 3*n +1
#     c+=1
#   print(n)
# print(c) 
#---------------------last Oc----------------------------
# def last(n:int,l:list,m:int):
  
# n = int(input())
# l = list(map(int,input().split()))
# m = int(input())
# -------------------------------------------------
# def Binary_Con(l:int) -> int:
#   t = []
#   if l == 0:
#     return "0"
#   while  l != 0:
#     r = l % 2
#     t.append(str(r))
#     l = l //  2
#   return ''.join(t[::-1])
# n = int(input())
# l = list(map(int,input().split()))
# k = int(input())
# d = 0
# for i in range(0, len(l)):
#   k1 = Binary_Con(i)
#   if k1.count('1') == k:
#     d += l[i]
# print(d)
# ------------------reverse----------------
# n = int(input())
# k = str(n)[::-1]
# print(k)
# i = 0
# j = len(k) - 1
# while i <= j:
#   k[i],k[j] = k[j],k[i]
#   i += 1
#   j -= 1
# if len(k) 
# print(''.join(map(str,list(k))))
# n = int(input())
# k = str(bin(n))[2::]
# ev = 0
# odd = 0
# for i in range(1,len(k)+1):
#   if (k[i-1] == '1') and ((i-1) % 2 == 0):
#     ev +=1
#   elif k[i-1] == '1' and (i-1) % 2 != 0:
#     odd += 1
# print([odd,ev])
# n = input()
# c = 0
# for i in n:
#   if i == '1':
#     c+=1
#   else:
#     if c > 0:
#       print(c)
#       print(chr(65+c-1))
#     c = 0
# if c > 0:
#   print(c)
# print(chr(c+65-1))
# n  = 984
# b = 10
# c = n / b
# print(float(c))
# n = int(input())
# c = 0
# for i in range(1,n):
#   for j in range(1,i):
#     c+=1
#     print(c,end =" ")
#   print("\r")
# n = int(input())
# if n % 4 == 0 and n % 400 == 0 and n % 100 != 0:
#   print("Leap Year")
# else:
#   print("NOT a LEAP YEAR")
# s = input()
# n = int(input())
# s1 = ""
# for i in range(len(s)):
#   s1 = s1 +str( ord(s[i])-96)
# for i in range(n):
#   for j in range(len(s1)):
# def spll(n):
#   k = n.strip().split("-")
#   return len(k[-1])
# n = input()
# print(spll(n))
# n = int(input())
# s =0
# for i in range(1,n-1):
#   if n % i == 0:
#     s+=i
#     print(s,i)
# x = int(input())
# l = list(map(int,input().split()))
# k = l[::2]
# o = l[1::2]
# print(o)
# n = int(input())
# for j in range(n):
#   m = int(input())
#   for j in range(m):
#     l = list(map(str,input().split()))
#     c = []
#     for k in range(len(l)):
#       if l[k] == '#':
#         c.append(k+1)
#     print(c[::-1],end=" ")
# n = int(input())
# for i in range(n):
#   a,b = map(int,input().split())
#   l = []
#   if a == b:
#     print(0)
#   else:
#     for j in range(a,b):
#       k = (j-a)+(b-j)
#       if k not in l:
#         l.append(k)
#     print(k)
# n = int(input())
# for _ in range(n):
#     m = input()
#     l=[]
#     if len(m) <= 10:
#         print(m)
#     else:
#       print(m[0],len(m)-2,m[-1],sep='')
# n = int(input())
# c = 0
# for _ in range(n):
#     l = list(map(int,input().split()))
#     k = l.count(1)
#     if k >= 2:
#         c += 1
# print(c)
n = int(input())
c = 0
for _ in range(n):
    m = input()
    if m == 'X++' or m == '++X':
        c += 1
    elif m == 'X--' or m == '--X':
        c -= 1
print(c)

