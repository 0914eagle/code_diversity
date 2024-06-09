
def get_median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def get_medians(numbers, excluding):
    medians = []
    for i in range(len(numbers)):
        if i == excluding:
            continue
        medians.append(get_median(numbers[:i] + numbers[i+1:]))
    return medians

def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N):
        print(get_medians(numbers, i)[-1])

if __name__ == '__main__':
    main()

