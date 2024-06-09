
def is_bus_service_available(s):
    # Check if the length of the string is 3
    if len(s) != 3:
        return "No"
    
    # Check if the string contains only A and B
    if not s.isalpha() or s.isdigit():
        return "No"
    
    # Check if there is a pair of stations that will be connected by a bus service
    if s[0] == "A" and s[2] == "B":
        return "Yes"
    elif s[0] == "B" and s[2] == "A":
        return "Yes"
    else:
        return "No"

