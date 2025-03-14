# n = input().split("+")
# l = []  
# for i in n:
#   l.append(i)
# l.sort()
# print("+".join(l))
# n = input()
# if n[0].isupper():
#   print(n)
# else:
#   n.lower()
#   print(n)
  # n.capitalize()
  # print(n)
# n = list(map(int,input().split()))
# p = int(input())
# s = []
# if sum(n) % p == 0:
#   print(0)
# elif sum(n) < p:
#   print(-1)
# else:
#   for i in range(len(n)):
#     for j in range(i+1,len(n)+1):
#       s = n[i:j]
#       if sum(s) == 17:
#         print(s)
# my_array = list(map(int,input().split()))
# n = len(my_array)
# for i in range(n-1):
#   for j in range(n-i-1):
#     if my_array[j] > my_array[j+1]:
#       my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
# print(my_array)
# a = list(map(int,input().split()))
# k = int(input())
# current_sum = 0
# start = 0
# end = 0
# c = 0
# while start <= end:
#   if current_sum < k:
#     end += 1
#     current_sum += a[end]
#   elif current_sum > k:
#     current_sum -= a[start]
#     start += 1
#   if current_sum == k:
#     c += 1
#     start += 1
# print(c)

# i = 0
# j = len(n) - 1
# c = 0
# while i < j:
#   if n[i] == n[j]:
#     i += 1
#     j -= 1
#   else:
#     c = 1
#     break
# if c == 0:
#   print("Palindrome")
# else:
#   print("Not a palidrome")
# arr1=[0]*26
# arr2=[0]*26
# s1=input().lower()
# s2=input().lower()
# for i in s1:
#     arr1[ord(i)-97]+=1
# for j in s2:
#     arr2[ord(j)-97]+=1
# print(arr1,arr2,sep='\n')
# if(arr1==arr2):
#     print('anagrams')
# else:
#     print('not a anagrams')
# n = input()
# d ={}
# l = ""
# for i in n:
#   if i not in d:
#     if i not in d:
#       d[i] = 1
#       l += (i)
#     else:
#       d[i] += 1
# print(l)
# n = input()
# i = 0
# c = 1
# j = i + 1
# l = ""
# while j < len(n): # 1 2 3 4  6 8 10 11 
#   if n[i] == n[j]: # a != b 
#     j += 1
#     c += 1# j = 11
#   else:
#     l += n[i]
#     l += str(c)
#     c = 1# [a,b,c,a,e]
#     i = j    # i = 11
#     j += 1   # j = 12
# l += n[-1]
# print(l+str(c)) 
# a a a a a b b c c a e d
#                       I 12
# n = input()
# d = {}
# l = ""
# for i in n:
#   if i not in d:
#     l  += 1
#     x  
# n = input()
# l = 0
# for i in range(1,len(n)-1,2):
#   if n[i] == 'C':
#     l = l ^ n[i+1]
#   elif n[i] == ''
# def Req_houses(rats,units,n,houses):
#   food = 0
#   if sum(houses) < rats * units:
#     return -1
#   for i in range(len(houses)):
#     food += houses[i]
#     if food >= rats * units:
#       return i + 1
# rats = int(input()) # 7
# units = int(input()) # 2
# n = int(input())
# houses = list(map(int,input().split()))#[8,2,1,4,3,2]
# print(Req_houses(rats,units,n,houses))
# def MAx_Product(n,arr):
#   i = 0
#   j = 0
#   max_product = 0
#   arr1 = set(arr) 
#   for k in range(len(arr)):
#     k1 = int(arr[k])
#     k2 = 18 - k1
#     if k2 in arr1:
#       if k1 * k2  > max_product:
#         max_product = k1 * k2
#         i = max(k1,k2)
#         j = min(k1,k2)
#   return [i,j]

# n = int(input())
# arr = list(map(int,input().split()))
# print(MAx_Product(n,arr))
# arr = list(map(int,input().split()))
# i = 0
# j = len(arr) - 1
# while i < j:
#   arr[i] , arr[j] = arr[j],arr[i]
#   i += 1
#   j -= 1
# # print(arr)
# def Max_Subarray(n,arr):
#   max_Sum = float("-inf")
#   current_sum = 0
#   for i in range(len(arr)):
#     current_sum += arr[i]
#     max_Sum = max(max_Sum,current_sum)
#     if current_sum < 0:
#       current_sum = 0
#   return max_Sum
# n = int(input())
# arr = list(map(int,input().split()))
# print(Max_Subarray(n,arr))
# def MAx_pro(n,arr):
#   arr1 = set(arr) #{10,11,8,7}
#   ma = 0
#   for i in range(len(arr)):#{11}
#     k = int(arr[i])# 10
#     k1 = 18 - int(arr[i]) # 18 - 11 --> 7
#     if k1 in arr1:
#       if ma < k * k1:#0 < 10 * 8 == 80
#         ma = k * k1
#         j = max(k,k1) #max(8,10) --> 10
#         j1 = min(k,k1) # 8
#   return [j,j1] # 10 8
# n = int(input())
# arr = list(map(int,input().split()))
# print(MAx_pro(n,arr))
# n = int(input())
# arr = [-2,1,-3,4,-1,2,1,-5,4]
# max_Sum = float("-inf")
# current_sum = 0
# for i in range(len(arr)):
#   current_sum += arr[i] # 1 -3 -->5
#   max_Sum = max(current_sum,max_Sum) # 6 , 5
#   if current_sum < 0:
#     current_sum = 0 # 0
# print(max_Sum) # 6
# def broken(n):
#   stack = []
#   for i in n:
#     if i != "#":
#       stack.append(i)
#     else:
#       stack.pop()
#   return stack
# n = input()
# m = input()
# if broken(n) == broken(m):
#   print("True")
# else:
#   print("False")
# input_stack = list(map(int,input().split()))
# stack = []
# result = [-1] * len(input_stack)
# for i in range(len(input_stack)-1,-1,-1):
#   while len(stack) != 0 and stack[-1] <= input_stack[i]:
#     stack.pop()
#   if stack:
#     result[i] = stack[-1]
#   stack.append(input_stack[i])
# print(result)
# class Node:
#     # Constructor method correction: __init__ instead of _init_
#     def __init__(self, data):
#         # Assign data to self.data, not next
#         self.data = data
#         self.next = None

# # Create nodes with data
# node1 = Node(10)
# node2 = Node(11)
# node3 = Node(14)

# # Link the nodes together
# node1.next = node2
# node2.next = node3

# # Traverse and print the linked list
# current_node = node1
# while current_node:
#     # Print the node's data, not the node itself
#     print(current_node.data, end=" -> ")
#     current_node = current_node.next
# print("Null")
# limark_we , bob_we = map(int,input().split())
# c = 0
# while limark_we <= bob_we:
#   c += 1
#   limark_we = limark_we * 3
#   bob_we = bob_we * 2
#   # print(limark_we,bob_we,end=' ')
# print(c)
# k,money,n = map(int,input().split())
# s = 0
# for i in range(1,n+1):
#     s += i * k
# if s > money:
#   print(abs(s - money))
# else:
#   print(0)
# n = int(input())
# mat = [list(map(int,input().split()))for _ in range(n)]
# result = [0*n]*n
# for i in range(len(mat)):
#   c = 0
#   for j in range(len(mat)):
#     mat[i][j] = mat[len(mat) - j - 1][i]
#     c += 1
#     print(mat,end=" ")
#   print("\n")
# n = eval(input())
# for i in n:
#   print(i)
# n = input()
# l = [0] * 26
# for i in range(len(n)):
#   l[ord(n[i]) - 97] += 1
# n = int(input().split())
# l = list(map(int,input().split()))
# print(*[l[i] for i in range(0,len(l),2)])
# def calculate_amount(N):
#   sum_of_digits = sum(int(digit) for digit in str(N))
#   reversed_sum = int(str(sum_of_digits)[::-1])
#   return reversed_sum
# n = int(input())
# print(calculate_amount(n))
# n = int(input())
# l = list(map(int,input().split()))
# m = int(input())
# l1 = list(map(int,input().split()))
# l2  = []
# for i in l:
#   if i not in l1:
#     l2.append(i)
# print(sum(l2)//len(l2))
# list_array = list(map(int,input().split()))
# number_of_time = int(input())
# if len(list_array) == number_of_time:
#   print(list_array)
# elif len(list_array) > number_of_time:
#   print(list_array[number_of_time:len(list_array)]+list_array[0:number_of_time])
# else:
#   print(list_array[(number_of_time % len(list_array)):len(list_array)] + list_array[0:(number_of_time % len(list_array))])
# n = int(input())
# k = str(bin(n))[2:]
# c = 0
# ma = 0
# for i in range(len(k)):
#   if k[i] == '1':
#     c = i - c
#     if c > ma:
#       ma = c
# print(ma) 
# arr = list(map(int,input().split()))
# n = len(arr)
# i = 0
# c = 0
# while i < n:
#   if arr[i] == 0:
#     print(c)
#     break
#   elif arr[i] <= n - i:
#     c += 1
#     i = arr[i]
#     print(i)
#   else:
#     break
# print(5^6^7^8^9)
#------------ maximum product  ------------------#
n = int(input())
l = list(map(int,input().split()))
i = 0
j = len(l) - 1
c = 0
while i < j: # 0 3
  if (l[i] + l[j]) % 4 == 0:
    j -= 1
    c += 1
  else:
    j -= 1
  if i >= j:
    i += 1
    j = len(l) - 1
print(c) 