
def get_input():
    return input()

def process_input(input_str):
    if input_str.isupper():
        return "A"
    else:
        return "a"

def main():
    input_str = get_input()
    result = process_input(input_str)
    print(result)

if __name__ == '__main__':
    main()

