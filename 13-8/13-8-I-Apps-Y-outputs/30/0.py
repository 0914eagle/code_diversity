
def get_efficacy(vaccinated_participants, control_participants):
    vaccinated_infected_strains = {}
    control_infected_strains = {}
    
    for participant in vaccinated_participants:
        for strain in participant[1:]:
            if strain == 'Y':
                if strain not in vaccinated_infected_strains:
                    vaccinated_infected_strains[strain] = 1
                else:
                    vaccinated_infected_strains[strain] += 1
    
    for participant in control_participants:
        for strain in participant[1:]:
            if strain == 'Y':
                if strain not in control_infected_strains:
                    control_infected_strains[strain] = 1
                else:
                    control_infected_strains[strain] += 1
    
    efficacy = {}
    for strain in vaccinated_infected_strains:
        if vaccinated_infected_strains[strain] < control_infected_strains[strain]:
            efficacy[strain] = (control_infected_strains[strain] - vaccinated_infected_strains[strain]) / control_infected_strains[strain]
        else:
            efficacy[strain] = "Not Effective"
    
    return efficacy

def main():
    num_participants = int(input())
    vaccinated_participants = []
    control_participants = []
    
    for _ in range(num_participants):
        participant = input()
        if participant[0] == 'Y':
            vaccinated_participants.append(participant)
        else:
            control_participants.append(participant)
    
    efficacy = get_efficacy(vaccinated_participants, control_participants)
    print(efficacy['A'])
    print(efficacy['B'])
    print(efficacy['C'])

if __name__ == '__main__':
    main()

