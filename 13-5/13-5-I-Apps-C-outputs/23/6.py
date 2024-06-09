
def get_lis_length(sequence):
    # implement your solution here
    return lis_length

def get_critical_elements(sequence):
    # implement your solution here
    return critical_elements

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    critical_elements = get_critical_elements(sequence)
    if critical_elements:
        print(*critical_elements)
    else:
        print(-1)

if __name__ == '__main__':
    main()

