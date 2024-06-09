
def find_harshad_number(n):
    while True:
        if n % sum(map(int, str(n))) == 0:
            return n
        n += 1

