# Project: Restaurant Order Management System

#* Classes

class Hospital:
    class Patient:
        def __init__(self, name, age, patient_id):
            self.name = name
            self.age = age
            self.patient_id = patient_id
            self.appointments = []

        def patient_details(self):
            return f'Name:{self.name} Age:{self.age}'

    class Staff:
        def __init__(self, name, department, staff_id):
            self.name = name
            self.department = department
            self.staff_id = staff_id

    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.staff = []
        self.patients = []

    def add_staff(self, name, department):
        staff_id = len(self.staff) + 1
        new_staff = self.Staff(name, department, staff_id)
        self.staff.append(new_staff)
        return new_staff

    def list_staff(self):
        for staff in self.staff:
            print(f'{staff.staff_id}. Dr. {staff.name} - {staff.department}')
    
    def add_patient(self, name, age):
        patient_id = len(self.patients) + 1
        new_patient = self.Patient(name, age, patient_id)
        self.patients.append(new_patient)
        return new_patient

    def check_patients(self, name):
        for patient in self.patients:
            if (name.lower() == patient.name.lower()):
                return ('Registred')
            
    def book_appointment(self, name, id, reason):
        # get doctors name
        for staff in self.staff:
            if (id == staff.staff_id):
                doctor_name = staff.name
                doctor_department = staff.department

        # get patient details
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                patient_main = patient

        # save appointment
        appointment_id = len(patient_main.appointments) + 1

        patient_main.appointments.append(
            {   'id' : appointment_id,
                'name': name,
                'reason': reason,
                'doctor_name': doctor_name,
                'doctor_department': doctor_department,
                'prescription': []
            })

        print( f'\nAppointment #{appointment_id} booked successfully for {name} 'f'with Dr. {doctor_name}({doctor_department}) for {reason}.')

    def appointment_history(self, name):
        # get patient details
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                patient_main = patient

        # return appointment history
        return patient_main.appointments

    def update_prescription(self, note_id, note, name):
        # get patient details
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                patient_main = patient

        # return appointment history
        all_appointments = patient_main.appointments
        for appointments in all_appointments:
            if appointments['id'] == int(note_id):
                appointments['prescription'].append(note)

#* Add Staff and Patients
hospital1 = Hospital('KaKa Hospital')

doctor1 = hospital1.add_staff('Bello','Cardiology')
doctor2 = hospital1.add_staff('Fatima', 'Optometry')
doctor3 = hospital1.add_staff('Mary', 'Emergency')
doctor4 = hospital1.add_staff('John', 'Radiology')
doctor5 = hospital1.add_staff('John', 'Radiology')
doctor6 = hospital1.add_staff('Adeyemi', 'Pediatrics')

patient1 = hospital1.add_patient('alamin', '22')
patient2 = hospital1.add_patient('john', '44')

# hospital1.list_staff()

#? State of the program
status = True

while status:
    # Starter Menu
    print('\n')
    print('Menu:')
    print('1. Register a patient')
    print('2. Book an appointment')
    print("3. View a patient's appointment history")
    print('4. Add a prescription note to an appointment')
    print('5. Exit')
    print('\n')
    user_input = input('Select from 1 - 5: ')

    # Validate user input
    user_input_valid = False

    while not user_input_valid:
        if user_input not in ['1', '2', '3', '4', '5']:
            print('Wrong Input!!!')
            user_input = input('Select from 1 - 5: ')
        else:
            user_input_valid = True

    # Route Based on input
    if user_input == '1':
        #? Register
        print('--- Registering a Patient ---')
        patient_name = input('Enter Patient Name: ')
        patient_age = input('Enter Patient Age: ')

        new_patient = hospital1.add_patient(patient_name, patient_age)

        print(f'Patient {new_patient.patient_id} registered successfully!')

    elif user_input == '2':
        #? Book Appointment
        # get patient name
        patient_appointment_name = input('Enter name of patient: ')

        # get patients list
        check = hospital1.check_patients(patient_appointment_name)

        # check if user is registered
        if check:
            # ask hich doctor the patinet wants to see
            hospital1.list_staff()

            # show all doctors
            patient_doctor_choice = int(input('Enter Doctors Number from menu: '))

            # asks for problems
            reason_for_visit = input('Reason for Visit: ')
    
            # save appointment
            hospital1.book_appointment(patient_appointment_name, patient_doctor_choice, reason_for_visit)
        else:
            print('Not Registered, Register using option 1')

    elif user_input == '3':
        #? View a patient's appointment history
        # get patient name
        patient_appointment_name = input('Enter name of patient: ')

        # get patients list
        check = hospital1.check_patients(patient_appointment_name)

        # check if user is registered
        if check:
            # check user appointment history
            appointments = hospital1.appointment_history(patient_appointment_name)

            # check and loop through
            if appointments == []:
                print('No appointment history yet')
            else:
                for appointment in appointments:
                    print('\n')
                    print(f"Patient: {appointment['name'].capitalize()}")
                    print(f"Reason for visit: {appointment['reason']}")
                    print(f"Dr. {appointment['doctor_name']}")
                    print(f"Department: {appointment['doctor_department']}")
                    if appointment['prescription'] == []:
                        print('No prescription Note')
                    else:
                        print(appointment['prescription'])

        else:
            print('Not Registered, Register using option 1')
        
    elif user_input == '4':
        #? Add prescription note
        # get patient name
        patient_appointment_name = input('Enter name of patient: ')
        
        # get patients list
        check = hospital1.check_patients(patient_appointment_name)
        
        # check if user is registered
        if check:
            # check user appointment history
            appointments = hospital1.appointment_history(patient_appointment_name)

            # check and loop through
            if appointments == []:
                print('No appointment history yet')
            else:
                # loop though all appointments
                for appointment in appointments:
                    print('\n')
                    print(appointment['id'])
                    print(f'Patient: {appointment['name'].capitalize()}')
                    print(f"Reason for visit: {appointment['reason']}")
                    print(f"Dr. {appointment['doctor_name']}")
                    print(f"Department: {appointment['doctor_department']}")
                    if appointment['prescription'] == []:
                        print('No prescription Note')
                    else:
                        print(appointment['prescription'])

            # ask what note
            print('\n')
            note_id = input('Select note you want to edit: ')
            note = input('Enter note you want to add: ')

            if check:
                hospital1.update_prescription(note_id, note, patient_appointment_name)
            
        else:
            print('Not Registered, Register using option 1')
    
    else:
        #? Exit
        print('\n')
        print('Goodbye 👋')
        status = False

