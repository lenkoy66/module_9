
def is_prime(func):
    def wrapper(a, b, c):
        sum_ = func(a, b, c)
        if sum_ <= 1:
            return 'Ни простое, ни составное'
        for n in range(2, int(sum_ ** 0.5) + 1):
            if sum_ % n == 0:
                return 'Составное'
        return 'Простое'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 4, 8)
print(result)