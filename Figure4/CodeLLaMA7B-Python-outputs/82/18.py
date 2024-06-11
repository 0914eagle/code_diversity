def prime_length(string):
    
    return len(string) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
