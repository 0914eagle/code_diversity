
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
        if vaccinated_infected < control_infected:
            vaccine_efficacy[strain] = round((1 - vaccinated_infected / control_infected) * 100, 2)
        else:
            vaccine_efficacy[strain] = "Not Effective"
    
    return vaccine_efficacy

def main():
    participants = []
    for _ in range(int(input())):
        participants.append(input())
    vaccine_efficacy = get_vaccine_efficacy(participants)
    print(vaccine_efficacy["A"])
    print(vaccine_efficacy["B"])
    print(vaccine_efficacy["C"])

if __name__ == '__main__':
    main()

