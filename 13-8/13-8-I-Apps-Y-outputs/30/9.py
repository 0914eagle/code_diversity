
def get_input():
    N = int(input())
    vaccinated = []
    control = []
    for i in range(N):
        participant = input()
        if participant[0] == 'Y':
            vaccinated.append(participant[1:])
        else:
            control.append(participant[1:])
    return vaccinated, control

def get_efficacy(vaccinated, control):
    vaccine_efficacy = []
    for i in range(3):
        vaccinated_strain = vaccinated.count(str(i))
        control_strain = control.count(str(i))
        if vaccinated_strain > control_strain:
            vaccine_efficacy.append(100 * (vaccinated_strain - control_strain) / control_strain)
        else:
            vaccine_efficacy.append('Not Effective')
    return vaccine_efficacy

def main():
    vaccinated, control = get_input()
    vaccine_efficacy = get_efficacy(vaccinated, control)
    print(vaccine_efficacy[0])
    print(vaccine_efficacy[1])
    print(vaccine_efficacy[2])

if __name__ == '__main__':
    main()

