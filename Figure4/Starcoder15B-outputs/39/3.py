def prime_fib(n: int):
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_list = [2, 3]
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
/README.md
# Prime Fibonacci

This is a simple program that returns the n-th number that is a Fibonacci number and it's also prime.

## Installation

Use the package manager [pip](https://pip.pypa.io/en