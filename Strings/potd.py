n = 5  # You can change this to any height you want
for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
  # Print spaces
  print(' ' * (n - i), end='')  # Print leading spaces
  # Print hashes
  print('#' * i)  