
def solve(numbers):
    sheet = set()
    for number in numbers:
        if number in sheet:
            sheet.remove(number)
        else:
            sheet.add(number)
    return len(sheet)

def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        N = int(input())
        numbers = [int(input()) for _ in range(N)]
        print(f"Case #{case}: {solve(numbers)}")

if __name__ == '__main__':
    main()

