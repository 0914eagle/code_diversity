
def f1(S):
    # Initialize the integer in Takahashi's mind to 0
    result = 0
    
    # Iterate through the string S and update the result accordingly
    for symbol in S:
        if symbol == "+":
            result += 1
        else:
            result -= 1
    
    # Return the result
    return result

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    S = input()
    result = f1(S)
    print(result)

