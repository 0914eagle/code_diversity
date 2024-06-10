
def get_number_of_sodas(e, f, c):
    total_empty_bottles = e + f
    return total_empty_bottles // c

def main():
    e, f, c = map(int, input().split())
    print(get_number_of_sodas(e, f, c))

if __name__ == '__main__':
    main()

