
def is_allowed_entry(numbers):
    for num in numbers:
        if num % 2 == 0 and num % 3 != 0 and num % 5 != 0:
            return "DENIED"
    return "APPROVED"

def main():
    numbers = list(map(int, input().split()))
    print(is_allowed_entry(numbers))

if __name__ == '__main__':
    main()

