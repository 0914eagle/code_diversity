
def process_string(text):
    result = ""
    for char in text:
        if char == "<":
            result = result[:-1]
        else:
            result += char
    return result

def main():
    text = input()
    print(process_string(text))

if __name__ == '__main__':
    main()

