def caching_fibonacci():
    cache = {}

    def fibonacci(n):

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif cache.get(n) == n:
            return cache[n]
        else:

            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


fib = caching_fibonacci()
