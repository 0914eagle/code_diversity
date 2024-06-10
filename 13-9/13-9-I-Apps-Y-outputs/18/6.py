
def is_valid_password(s, p):
    if s == p:
        return True
    if p.startswith(s):
        return True
    if p.endswith(s):
        return True
    if p.lower() == s.lower():
        return True
    return False

def main():
    s = input("Enter stored password: ")
    p = input("Enter attempted password: ")
    if is_valid_password(s, p):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

