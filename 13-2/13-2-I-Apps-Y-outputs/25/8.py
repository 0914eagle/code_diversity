
def is_connected(s):
    # Check if the input string has length 3
    if len(s) != 3:
        return "No"
    
    # Check if the input string contains only 'A' and 'B'
    if not all(c in ["A", "B"] for c in s):
        return "No"
    
    # Check if there is a pair of stations that will be connected by a bus service
    if s[0] == "A" and s[2] == "B":
        return "Yes"
    elif s[0] == "B" and s[1] == "A":
        return "Yes"
    elif s[1] == "A" and s[2] == "B":
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    s = input()
    print(is_connected(s))

