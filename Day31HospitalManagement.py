import pickle
import os

# ---------------- PATIENT ----------------

def addPatient():
    with open('patient.bin', 'ab') as file:
        pid = input("\tEnter Patient ID: ")
        name = input("\tEnter Name: ")
        address = input("\tEnter Address: ")
        mobile = input("\tEnter Mobile: ")
        disease = input("\tEnter Disease: ")

        patient = {
            "pid": pid,
            "name": name,
            "address": address,
            "mobile": mobile,
            "disease": disease
        }

        pickle.dump(patient, file)

    print("\tPatient added successfully\n")


def viewPatients():
    if not os.path.exists("patient.bin"):
        print("\tNo records found\n")
        return

    with open('patient.bin', 'rb') as file:
        print("\n\tPatient Records:\n")
        print("\t{:<10} {:<15} {:<15} {:<15} {:<10}".format("ID","Name","Address","Mobile","Disease"))
        print("-"*70)

        try:
            while True:
                data = pickle.load(file)
                print("\t{:<10} {:<15} {:<15} {:<15} {:<10}".format(
                    data["pid"], data["name"], data["address"], data["mobile"], data["disease"]
                ))
        except EOFError:
            pass
    print()


def deletePatient():
    if not os.path.exists("patient.bin"):
        print("\tNo records found\n")
        return

    pid = input("\tEnter Patient ID to delete: ")
    found = False

    with open('patient.bin', 'rb') as file1, open('temp.bin', 'ab') as file2:
        try:
            while True:
                data = pickle.load(file1)
                if data["pid"] != pid:
                    pickle.dump(data, file2)
                else:
                    found = True
        except EOFError:
            pass

    os.remove('patient.bin')
    os.rename('temp.bin', 'patient.bin')

    if found:
        print("\tPatient deleted\n")
    else:
        print("\tPatient not found\n")


# ---------------- DOCTOR ----------------

def addDoctor():
    with open('doctor.bin', 'ab') as file:
        did = input("\tEnter Doctor ID: ")
        name = input("\tEnter Name: ")
        spec = input("\tEnter Specialization: ")

        doctor = {
            "did": did,
            "name": name,
            "spec": spec
        }

        pickle.dump(doctor, file)

    print("\tDoctor added successfully\n")


def viewDoctors():
    if not os.path.exists("doctor.bin"):
        print("\tNo records found\n")
        return

    with open('doctor.bin', 'rb') as file:
        print("\n\tDoctor Records:\n")
        print("\t{:<10} {:<15} {:<20}".format("ID","Name","Specialization"))
        print("-"*50)

        try:
            while True:
                data = pickle.load(file)
                print("\t{:<10} {:<15} {:<20}".format(
                    data["did"], data["name"], data["spec"]
                ))
        except EOFError:
            pass
    print()


def updateDoctor():
    if not os.path.exists("doctor.bin"):
        print("\tNo records found\n")
        return

    did = input("\tEnter Doctor ID to update: ")
    found = False

    with open('doctor.bin', 'rb') as file1, open('temp.bin', 'ab') as file2:
        try:
            while True:
                data = pickle.load(file1)
                if data["did"] == did:
                    print("\tEnter new details:")
                    data["name"] = input("\tNew Name: ")
                    data["spec"] = input("\tNew Specialization: ")
                    found = True
                pickle.dump(data, file2)
        except EOFError:
            pass

    os.remove('doctor.bin')
    os.rename('temp.bin', 'doctor.bin')

    if found:
        print("\tDoctor updated successfully\n")
    else:
        print("\tDoctor not found\n")


# ---------------- HELPERS ----------------

def getPatient(pid):
    if not os.path.exists("patient.bin"):
        return None

    with open('patient.bin', 'rb') as file:
        try:
            while True:
                data = pickle.load(file)
                if data["pid"] == pid:
                    return data
        except EOFError:
            pass
    return None


def getDoctor(did):
    if not os.path.exists("doctor.bin"):
        return None

    with open('doctor.bin', 'rb') as file:
        try:
            while True:
                data = pickle.load(file)
                if data["did"] == did:
                    return data
        except EOFError:
            pass
    return None


# ---------------- APPOINTMENT ----------------

def bookAppointment():
    pid = input("Enter Patient ID: ")
    patient = getPatient(pid)

    if patient is None:
        print("\tPatient not found\n")
        return

    did = input("\tEnter Doctor ID: ")
    doctor = getDoctor(did)

    if doctor is None:
        print("\tDoctor not found\n")
        return

    date = input("\tEnter Appointment Date: ")

    appointment = {
        "pid": pid,
        "did": did,
        "date": date
    }

    with open('appointment.bin', 'ab') as file:
        pickle.dump(appointment, file)

    print("\tAppointment booked successfully\n")


def viewAppointments():
    if not os.path.exists("appointment.bin"):
        print("\tNo records found\n")
        return

    with open('appointment.bin', 'rb') as file:
        print("\n\tAppointments:\n")

        try:
            while True:
                data = pickle.load(file)
                patient = getPatient(data["pid"])
                doctor = getDoctor(data["did"])

                if patient and doctor:
                    print("\tPatient:", patient["name"])
                    print("\tDoctor:", doctor["name"])
                    print("\tDate:", data["date"])
                    print("\t----------------------")
        except EOFError:
            pass
    print()


def viewAppointmentsByPID():
    pid = input("\tEnter Patient ID: ")
    found = False

    if not os.path.exists("appointment.bin"):
        print("\tNo records found\n")
        return

    with open('appointment.bin', 'rb') as file:
        try:
            while True:
                data = pickle.load(file)
                if data["pid"] == pid:
                    doctor = getDoctor(data["did"])
                    print("\tDoctor:", doctor["name"])
                    print("\tDate:", data["date"])
                    print("\t----------------------")
                    found = True
        except EOFError:
            pass

    if not found:
        print("\tNo appointments found\n")
    else:
        print()


# ---------------- MENU ----------------

while True:
    print("\t===== Hospital Management System =====")
    print('''
            1. Add Patient
            2. View Patients
            3. Delete Patient
            4. Add Doctor
            5. View Doctors
            6. Update Doctor
            7. Book Appointment
            8. View Appointments
            9. View Appointments by Patient ID
            0. Exit
            ''')
        

    choice = input("Enter your choice: ")

    if choice == "1":
        addPatient()
    elif choice == "2":
        viewPatients()
    elif choice == "3":
        deletePatient()
    elif choice == "4":
        addDoctor()
    elif choice == "5":
        viewDoctors()
    elif choice == "6":
        updateDoctor()
    elif choice == "7":
        bookAppointment()
    elif choice == "8":
        viewAppointments()
    elif choice == "9":
        viewAppointmentsByPID()
    elif choice == "0":
        print("\tBye Bye Admin!")
        break
    else:
        print("\tInvalid choice\n")
