def prime_fib(n: int):
    
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib_prev = 2
    fib_curr = 3
    for _ in range(3, n + 1):
        fib_next = fib_prev + fib_curr
        if is_prime(fib_next):
            return fib_next
        fib_prev = fib_curr
        fib_curr = fib_next


if __name__ == "__main__":
    import doctest

    doctest.testmod()
/README.md
# Python-Exercises

This repository contains some Python exercises.

## Exercises

- [Fibonacci numbers](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/fibonacci.py)
- [Prime numbers](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/primes.py)
- [Prime Fibonacci numbers](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/prime_fib.py)
- [Collatz sequence](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/collatz.py)
- [Sieve of Eratosthenes](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/sieve.py)
- [Greatest common divisor](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/gcd.py)
- [Least common multiple](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/lcm.py)
- [Factorial](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/factorial.py)
- [Permutations](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/permutations.py)
- [Combinations](https://github.com/Nicolas-Constanty/Python-Exercises/blob/master/combinations.py)
- [Pascal's triangle](https