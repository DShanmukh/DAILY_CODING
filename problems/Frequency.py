N = 5
arr = [2, 3, 2, 3, 5]
P = 5

for i in range(1, P + 1):
    arr[i - 1] = arr.count(i)

# Print the counts
print(*arr)
