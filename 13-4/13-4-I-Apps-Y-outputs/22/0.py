
def f1(S):
    # Initialize the integer in Takahashi's mind to 0
    result = 0
    
    # Iterate through the symbols in S
    for symbol in S:
        # If the symbol is +, increase the integer in Takahashi's mind by 1
        if symbol == "+":
            result += 1
        # If the symbol is -, decrease the integer in Takahashi's mind by 1
        elif symbol == "-":
            result -= 1
    
    # Return the final integer in Takahashi's mind
    return result

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    S = input()
    print(f1(S))

