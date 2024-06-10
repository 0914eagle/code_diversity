
def get_vaccine_efficacy(num_participants, participants):
    vaccinated_group = []
    control_group = []
    for participant in participants:
        if participant[0] == 'Y':
            vaccinated_group.append(participant)
        else:
            control_group.append(participant)
    
    vaccine_efficacy = {}
    for strain in ['A', 'B', 'C']:
        vaccinated_count = 0
        control_count = 0
        for participant in vaccinated_group:
            if participant[strain] == 'Y':
                vaccinated_count += 1
        for participant in control_group:
            if participant[strain] == 'Y':
                control_count += 1
        if control_count == 0:
            vaccine_efficacy[strain] = 0
        else:
            vaccine_efficacy[strain] = (vaccinated_count / len(vaccinated_group)) / (control_count / len(control_group))
    
    return vaccine_efficacy

def main():
    num_participants = int(input())
    participants = []
    for _ in range(num_participants):
        participants.append(input())
    vaccine_efficacy = get_vaccine_efficacy(num_participants, participants)
    print(f"Vaccine Efficacy against strain A: {vaccine_efficacy['A']:.2f}")
    print(f"Vaccine Efficacy against strain B: {vaccine_efficacy['B']:.2f}")
    print(f"Vaccine Efficacy against strain C: {vaccine_efficacy['C']:.2f}")

if __name__ == '__main__':
    main()

