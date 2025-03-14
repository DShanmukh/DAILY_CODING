n= input()
l = []
i = 0
while i < len(n):
  if n[i].isdigit():
    j = i
    while j <len(n) and n[j].isdigit():
      j += 1
    l.append(n[i:j])
    i = j
  else:
    i += 1
print(l)