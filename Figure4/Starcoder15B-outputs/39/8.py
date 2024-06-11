def prime_fib(n: int):
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a = 2
        b = 3
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
        return c


if __name__ == "__main__":
    import doctest
    doctest.testmod()
/README.md
# prime-fibonacci

## Description

This is a simple program that returns the n-th number that is a Fibonacci number and it's also prime.

## Usage

```
