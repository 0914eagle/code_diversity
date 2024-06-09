
import sys
import heapq

class Patient:
    def __init__(self, name, arrival_time, severity):
        self.name = name
        self.arrival_time = arrival_time
        self.severity = severity
        self.waiting_time = 0

    def __lt__(self, other):
        if self.severity == other.severity:
            return self.name < other.name
        return self.severity > other.severity

def f1(arrival_time, name, severity):
    # Process a patient arrival to the clinic
    patient = Patient(name, arrival_time, severity)
    patients.append(patient)

def f2(time):
    # At time T, the doctor is ready to treat a patient
    if not patients:
        return "doctor takes a break"
    patient = heapq.heappop(patients)
    patient.waiting_time = time - patient.arrival_time
    return patient.name

def f3(time, name):
    # At time T, the clinic receives a notification stating that, due to unfortunate circumstances, a patient with name M has left the queue permanently
    for i in range(len(patients)):
        if patients[i].name == name:
            patients.pop(i)
            break

patients = []
K = 0

for line in sys.stdin:
    query = line.split()
    if query[0] == "1":
        f1(int(query[1]), query[2], int(query[3]))
    elif query[0] == "2":
        print(f2(int(query[1])))
    elif query[0] == "3":
        f3(int(query[1]), query[2])


