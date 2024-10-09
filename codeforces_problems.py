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
a = list(map(int,input().split()))
k = int(input())
current_sum = 0
start = 0
end = 0
c = 0
while start <= end:
  if current_sum < k:
    end += 1
    current_sum += a[end]
  elif current_sum > k:
    current_sum -= a[start]
    start += 1
  if current_sum == k:
    c += 1
    start += 1
print(c)