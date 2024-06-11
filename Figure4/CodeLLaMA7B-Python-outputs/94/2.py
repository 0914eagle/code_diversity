def skjkasdkd(lst):
    
    # Step 1: Create a list of prime numbers
    prime_lst = []
    for i in lst:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_lst.append(i)
    # Step 2: Find the largest prime number
    largest_prime = max(prime_lst)
    # Step 3: Find the sum of the digits of the largest prime number
    sum_of_digits = sum([int(i) for i in str(largest_prime)])
    return sum_of_digits


if __name__ == '__main__':
    print(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
    print(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]))
    print(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]))
    print(skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]))
    print(skjkasdkd([0, 81, 12, 3, 1, 21]))
    print(skjkasdkd([0, 8, 1, 2, 1, 7]))
