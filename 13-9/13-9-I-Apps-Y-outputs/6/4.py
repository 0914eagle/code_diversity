
def find_harshad_number(n):
    while True:
        if sum(int(i) for i in str(n)) == 0:
            return n
        n += 1

assert find_harshad_number(24) == 24
assert find_harshad_number(25) == 27

