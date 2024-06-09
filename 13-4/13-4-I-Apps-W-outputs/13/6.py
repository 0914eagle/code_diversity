
import sys

class Patient:
    def __init__(self, name, severity, arrival_time):
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time
        self.waiting_time = 0

    def __lt__(self, other):
        return self.severity + K * self.waiting_time < other.severity + K * other.waiting_time

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

def process_arrival(arrival_time, name, severity):
    patient = Patient(name, severity, arrival_time)
    patients.append(patient)

def process_treatment(treatment_time):
    global patients
    if not patients:
        print("doctor takes a break")
        return
    patients.sort(reverse=True)
    patient = patients.pop()
    patient.waiting_time = treatment_time - patient.arrival_time
    print(patient)

def process_notification(notification_time, name):
    global patients
    for patient in patients:
        if patient.name == name:
            patients.remove(patient)
            return

patients = []
K = 0

for line in sys.stdin:
    query = line.split()
    if query[0] == "1":
        process_arrival(int(query[1]), query[2], int(query[3]))
    elif query[0] == "2":
        process_treatment(int(query[1]))
    elif query[0] == "3":
        process_notification(int(query[1]), query[2])


