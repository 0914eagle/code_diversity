
def calculate_sum(n):
    # Calculate the sum of all integers from 1 to n
    sum = (n * (n + 1)) // 2
    
    # Subtract the powers of two from the sum
    for i in range(n.bit_length()):
        sum -= 2 ** i
    
    return sum

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(calculate_sum(n))

if __name__ == '__main__':
    main()

