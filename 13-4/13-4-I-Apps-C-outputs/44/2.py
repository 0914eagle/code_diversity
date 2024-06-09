
n = int(input())
people = []
buttons = []

for i in range(n):
    line = input()
    people.append([int(j) for j in line])
    buttons.append([int(j) for j in line])

def count_people_on_button(button):
    count = 0
    for person in people:
        if person[button-1] == 1:
            count += 1
    return count

def count_buttons_for_person(person):
    count = 0
    for button in buttons:
        if button[person-1] == 1:
            count += 1
    return count

def is_valid_configuration(configuration):
    for i in range(n):
        person = configuration[i]
        button = i+1
        if count_people_on_button(button) > 1 or count_buttons_for_person(person) > 1:
            return False
    return True

def get_valid_configurations():
    valid_configurations = []
    for i in range(n):
        for j in range(n):
            configuration = [0] * n
            configuration[i] = j+1
            if is_valid_configuration(configuration):
                valid_configurations.append(configuration)
    return valid_configurations

def get_max_configurations():
    valid_configurations = get_valid_configurations()
    max_configurations = 0
    for configuration in valid_configurations:
        count = 0
        for i in range(n):
            person = configuration[i]
            button = i+1
            if count_people_on_button(button) == 1 and count_buttons_for_person(person) == 1:
                count += 1
        if count > max_configurations:
            max_configurations = count
    return max_configurations

def get_configuration_string(configuration):
    return " ".join([str(i+1) for i in configuration])

def get_configuration_strings(valid_configurations):
    return [get_configuration_string(configuration) for configuration in valid_configurations]

max_configurations = get_max_configurations()
print(max_configurations)
print("\n".join(get_configuration_strings(get_valid_configurations())))

