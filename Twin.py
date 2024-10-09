n = int(input())
l = []
k = []
for i in range(2, n):
    is_prime_i = True
    is_prime_i_plus_2 = True

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime_i = False
            break

    for j in range(2, int((i + 2) ** 0.5) + 1):
        if (i + 2) % j == 0:
            is_prime_i_plus_2 = False
            break

    if is_prime_i and is_prime_i_plus_2:
        k.append(i)
        k.append(i + 2)

print(*k)
