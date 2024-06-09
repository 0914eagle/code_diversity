
def harshad_number(n):
    while True:
        if sum(int(i) for i in str(n)) == 0:
            return n
        n += 1

n = int(input())
print(harshad_number(n))

