def fibonacci(n):
    if n == 0:
        return ValueError
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


for i in range(20):
    print(fibonacci(i))