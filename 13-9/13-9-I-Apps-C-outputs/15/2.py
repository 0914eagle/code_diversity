
def get_max_score(numbers):
    # Your code here
    return max_score

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    max_score = get_max_score(numbers)
    print(max_score)

if __name__ == '__main__':
    main()

