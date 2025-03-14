input_array = list(map(int,input().split()))
stack = []
input_array.sort()
for i in range(len(input_array)):
  stack.append(input_array[i])
while len(stack) > 1:
  if stack[-1] == stack[-2] and len(stack) != 0:
    k = stack.pop()
    k1 = stack.pop()
    stack.append(0)
    stack.sort()
  elif (stack[-1] > stack[-2]) and len(stack) != 0:
    k = stack.pop()
    k1 = stack.pop()
    stack.append(abs(k-k1))
    stack.sort()
print(stack)