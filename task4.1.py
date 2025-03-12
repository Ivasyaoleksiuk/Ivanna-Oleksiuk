def fib_generator():
    x, y = 0, 1

    while True:
        yield x
        x, y = y, x + y


fib_seq = fib_generator()

print("Перші 10 чисел Фібоначчі:")
for _ in range(10):
    print(next(fib_seq), end=' ')
