#smallest One
# array = list(map(int,input().split()))
# minimum = max(array)
# for i in array:
#   if i <= minimum:
#     minimum = i
# print(minimum)
# ----------------- Binary TO decimal ----------------------
# n = input()
# counter = 0
# decimal_sum = 0
# for i in range(len(n) - 1, -1,-1):
#   decimal_sum += (2 ** counter)
#   counter += 1
# print(decimal_sum)
# ------------------ decimal to Binary -------------------------
# n = int(input())
# l =[]
# while n != 0:
#   k = n % 2
#   l.append(k)
#   n = n // 2
# print("".join(map(str,l[::-1]))) 
