prime_list = []

for num in range(2,11):
    is_prime = True
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            prime_list.append(num)


print(prime_list)