
def find_harshad_number(n):
    sum_of_digits = 0
    while True:
        sum_of_digits = sum(int(i) for i in str(n))
        if n % sum_of_digits == 0:
            return n
        n += 1

