
def calculate_sum(n):
    sum = 0
    for i in range(1, n+1):
        if i == 2**(i.bit_length()-1):
            sum -= i
        else:
            sum += i
    return sum

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(calculate_sum(n))

if __name__ == '__main__':
    main()

