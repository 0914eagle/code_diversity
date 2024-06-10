
def get_number_of_digits(estimate):
    return len(str(estimate))

def main():
    num_estimates = int(input())
    for i in range(num_estimates):
        estimate = int(input())
        print(get_number_of_digits(estimate))

if __name__ == '__main__':
    main()

