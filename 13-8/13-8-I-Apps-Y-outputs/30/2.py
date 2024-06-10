
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
        vaccinated_infected_count = 0
        control_infected_count = 0
        for participant in vaccinated_group:
            if participant[strain] == "Y":
                vaccinated_infected_count += 1
        for participant in control_group:
            if participant[strain] == "Y":
                control_infected_count += 1
        if vaccinated_infected_count < control_infected_count:
            vaccine_efficacy[strain] = (control_infected_count - vaccinated_infected_count) / control_infected_count
        else:
            vaccine_efficacy[strain] = "Not Effective"
    
    return vaccine_efficacy

def main():
    num_participants = int(input())
    participants = []
    for _ in range(num_participants):
        participant = input()
        participants.append(participant)
    
    vaccine_efficacy = get_vaccine_efficacy(participants)
    print("Vaccine Efficacy:")
    for strain in ["A", "B", "C"]:
        print(f"{strain}: {vaccine_efficacy[strain]}")

if __name__ == '__main__':
    main()

