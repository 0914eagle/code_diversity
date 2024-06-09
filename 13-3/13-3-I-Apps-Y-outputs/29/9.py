
def get_parity(n):
    return n % 2

def get_sum_of_k_numbers(n, k):
    if k == 1:
        return [n]
    
    parity = get_parity(n)
    sum_of_k_numbers = []
    for i in range(1, k+1):
        if get_parity(i) == parity:
            sum_of_k_numbers.append(i)
    
    return sum_of_k_numbers

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        sum_of_k_numbers = get_sum_of_k_numbers(n, k)
        if sum_of_k_numbers:
            print("YES")
            print(" ".join(map(str, sum_of_k_numbers)))
        else:
            print("NO")

if __name__ == '__main__':
    main()

