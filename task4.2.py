import time

def time_tracker(func):
    def inner(count):
        start = time.time()
        result = func(count)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return inner

def find_primes():
    num = 2
    while True:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            yield num
        num += 1

@time_tracker
def get_prime_numbers(count):
    prime_list = []
    prime_gen = find_primes()
    for _ in range(count):
        prime_list.append(next(prime_gen))
    print(prime_list)
    return prime_list

get_prime_numbers(10)