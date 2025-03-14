n = input()
n_list = list(n)

i, j = 0, len(n_list) - 1

while i < j:
    if not n_list[i].isalpha():
        i += 1
    elif not n_list[j].isalpha():
        j -= 1
    else:
        n_list[i], n_list[j] = n_list[j], n_list[i]
        i += 1
        j -= 1

result = ''.join(n_list)
print(result)
