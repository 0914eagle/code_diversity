
def get_median(numbers):
    numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        return (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        return numbers[length // 2]

def get_medians(numbers, excluded):
    medians = []
    for i in range(len(numbers)):
        if i not in excluded:
            medians.append(get_median(numbers[:i] + numbers[i+1:]))
    return medians

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    excluded = set()
    for i in range(n):
        excluded.add(i)
        print(get_medians(numbers, excluded))
        excluded.remove(i)

if __name__ == '__main__':
    main()

