def contains(number):
    for digit in str(number):
        if int(digit) % 2 == 0:
            return False
    return True

def next(number):
    next_number = number + 1
    while not contains(next_number):
        next_number += 1
    return next_number
n = int(input())
for i in range(n):
  input_number = int(input())
  nextq= next(input_number)
  print(nextq)
