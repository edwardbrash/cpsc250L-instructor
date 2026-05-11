import time
#from functools import lru_cache
#@lru_cache(maxsize=32)

def fib_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def time_function(function, n):
    start_time = time.time()
    function(n)
    end_time = time.time()
    return end_time - start_time


def main():
    values = [5, 10, 20, 25, 30, 35, 40]

    print("Fibonacci Timing")
    print("----------------")
    print("n    recursive_time    iterative_time")

    nterms = []
    rtime = []
    itime = []
    for n in values:
        recursive_time = time_function(fib_recursive, n)
        iterative_time = time_function(fib_iterative, n)
        print(f"{n:<5} {recursive_time:.6f} seconds    {iterative_time:.6f} seconds")
        nterms.append(n)
        itime.append(iterative_time)
        rtime.append(recursive_time)

    import matplotlib.pyplot as plt
    plt.plot(nterms, rtime, label='Recursive Time', marker='o')
    plt.plot(nterms, itime, label='Iterative Time', marker='o')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.yscale('log')
    plt.show()


main()
