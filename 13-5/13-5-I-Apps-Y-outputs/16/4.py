
def is_bus_service_available(s):
    if s[0] == "A" and s[2] == "B":
        return "Yes"
    elif s[0] == "B" and s[2] == "A":
        return "Yes"
    else:
        return "No"

