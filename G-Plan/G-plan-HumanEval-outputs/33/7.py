
def strlen(string: str) -> int:
    length = 0
    for char in string:
        length += 1
    return length

# Main function to read input and call the strlen function
def main():
    input_string = input().strip()
    result = strlen(input_string)
    print(result)

if __name__ == "__main__":
    main()
