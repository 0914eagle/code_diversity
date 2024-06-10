
def sum_of_powers_of_two(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum -= 2**i
        else:
            sum += 2**i
    return sum

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(sum_of_powers_of_two(n))

if __name__ == '__main__':
    main()

