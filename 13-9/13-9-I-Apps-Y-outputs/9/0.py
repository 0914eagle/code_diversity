
def get_magnitude(estimate):
    return len(str(estimate))

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        estimate = int(input())
        magnitude = get_magnitude(estimate)
        print(magnitude)

if __name__ == '__main__':
    main()

