
def f1(S):
    # Initialize the integer in Takahashi's mind to 0
    mind = 0
    
    # Iterate through the string S and update the integer in Takahashi's mind accordingly
    for symbol in S:
        if symbol == "+":
            mind += 1
        else:
            mind -= 1
    
    # Return the final integer in Takahashi's mind
    return mind

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    S = input()
    print(f1(S))

