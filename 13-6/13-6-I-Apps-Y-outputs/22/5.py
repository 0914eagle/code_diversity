
def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def get_medians(numbers, excluded):
    medians = []
    for i in range(len(numbers)):
        if i not in excluded:
            medians.append(get_median(numbers[:i] + numbers[i+1:]))
    return medians

def solve(numbers):
    N = len(numbers)
    medians = get_medians(numbers, [])
    return [medians[i] for i in range(N)]

if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    print(*solve(numbers), sep='\n')

