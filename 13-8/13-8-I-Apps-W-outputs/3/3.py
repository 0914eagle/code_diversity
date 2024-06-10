
def get_remainder(L, A, B, M):
    # Calculate the terms of the arithmetic progression
    terms = [A + B * i for i in range(L)]
    
    # Convert the terms to strings
    terms_str = [str(term) for term in terms]
    
    # Concatenate the terms into a single string
    concatenated_str = "".join(terms_str)
    
    # Convert the concatenated string to an integer
    concatenated_int = int(concatenated_str)
    
    # Calculate the remainder when the integer is divided by M
    remainder = concatenated_int % M
    
    return remainder

def main():
    L, A, B, M = map(int, input().split())
    print(get_remainder(L, A, B, M))

if __name__ == '__main__':
    main()

