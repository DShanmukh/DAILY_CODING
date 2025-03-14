n = list(map(int,input().split()))
appending_stack = []
pop_stack = []
for i in range(len(n)):
  appending_stack.append(n[i])
while appending_stack:
  pop_stack.append(appending_stack.pop())
while pop_stack:
  print(pop_stack.pop())