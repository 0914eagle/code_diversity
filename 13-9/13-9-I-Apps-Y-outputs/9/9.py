
def get_estimate_magnitude(estimate):
    return len(str(estimate))

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        estimate = int(input())
        print(get_estimate_magnitude(estimate))

if __name__ == '__main__':
    main()

