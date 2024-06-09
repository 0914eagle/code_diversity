
def solve(john_marie_input, doctor_input):
    john_marie_count = 0
    doctor_count = 0
    for i in range(len(john_marie_input)):
        if john_marie_input[i] == "a":
            john_marie_count += 1
        if doctor_input[i] == "a":
            doctor_count += 1
    if john_marie_count >= doctor_count:
        return "go"
    else:
        return "no"

