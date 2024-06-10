
def is_uppercase(alpha):
    return alpha.isupper()

def convert_letter(alpha):
    if is_uppercase(alpha):
        return "A"
    else:
        return "a"

if __name__ == "__main__":
    alpha = input()
    print(convert_letter(alpha))

