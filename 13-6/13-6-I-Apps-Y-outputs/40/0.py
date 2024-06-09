
def get_max_divisible_elements(a):
    # Your code here
    return max_divisible_elements

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        max_divisible_elements = get_max_divisible_elements(a)
        print(max_divisible_elements)

if __name__ == '__main__':
    main()

