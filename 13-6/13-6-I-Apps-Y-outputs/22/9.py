
def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def get_medians(numbers, excluded_index):
    medians = []
    for i in range(len(numbers)):
        if i != excluded_index:
            medians.append(get_median(numbers[:i] + numbers[i+1:]))
    return medians

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    for i in range(n):
        print(get_medians(numbers, i)[i])

if __name__ == '__main__':
    main()

