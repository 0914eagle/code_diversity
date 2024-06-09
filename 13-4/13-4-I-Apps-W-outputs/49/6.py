
def get_sequence_element(n):
    i = 1
    while i < n:
        i += i
    return i

def main():
    n = int(input())
    print(get_sequence_element(n))

if __name__ == '__main__':
    main()

