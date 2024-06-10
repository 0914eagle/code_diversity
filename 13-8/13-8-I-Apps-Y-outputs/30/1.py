
def get_vaccine_efficacy(participants):
    vaccinated_group = []
    control_group = []
    for participant in participants:
        if participant[0] == "Y":
            vaccinated_group.append(participant)
        else:
            control_group.append(participant)
    
    vaccine_efficacy = {}
    for strain in ["A", "B", "C"]:
        vaccinated_infected = 0
        control_infected = 0
        for participant in vaccinated_group:
            if participant[strain] == "Y":
                vaccinated_infected += 1
        for participant in control_group:
            if participant[strain] == "Y":
                control_infected += 1
        if vaccinated_infected == 0 or control_infected == 0:
            vaccine_efficacy[strain] = "Not Effective"
        else:
            vaccine_efficacy[strain] = (vaccinated_infected / len(vaccinated_group)) / (control_infected / len(control_group))
    
    return vaccine_efficacy

def main():
    participants = []
    for _ in range(int(input())):
        participants.append(input())
    vaccine_efficacy = get_vaccine_efficacy(participants)
    for strain in ["A", "B", "C"]:
        print(vaccine_efficacy[strain])

if __name__ == '__main__':
    main()

