
def find_harshad_number(n):
    while True:
        if sum(int(digit) for digit in str(n)) == 0:
            return n
        n += 1

