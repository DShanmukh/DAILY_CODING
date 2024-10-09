n = input()
n = list(n)  # Convert the string to a list so that it can be modified

i = 0
j = len(n) - 1

while i < j:
    if n[i] in ['a', 'e', 'i', 'o', 'u']:
        while j > i and n[j] not in ['a', 'e', 'i', 'o', 'u']:
            j -= 1
        n[i], n[j] = n[j], n[i]
        j -= 1
    i += 1

result = ''.join(n)
print(result)
