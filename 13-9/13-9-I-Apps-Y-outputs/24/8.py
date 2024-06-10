
def get_max_diff(numbers):
    max_diff = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def main():
    numbers = list(map(int, input().split()))
    print(get_max_diff(numbers))

if __name__ == '__main__':
    main()

