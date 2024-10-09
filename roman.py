n = input()
d = {
  "I":1,
  "V":5,
  "X":10,
  "L":50,
  "C":100,
  "D":500,
  "M":1000
}
r = 0 
for i in range(len(n)):
  if i+1 < len(n) and d[n[i]] < d[n[i+1]]:
    r -= d[n[i]]
  else:
    r += d[n[i]]
print(r)