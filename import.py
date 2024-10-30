import csv

def load_contacts(filename):
    contacts = {}
    with open(filename, mode = 'r', newline= '') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:

            first_name = row [0]
            last_name = row[1]
            phone_number = row[2]
            email = row[3]
            contacts[last_name] = [first_name, last_name, phone_number, email]
        return contacts

def display_contact_info(contact_info):
    if contact_info:
        print('\nContact Information: ')
        print(f'First Name : {contact_info[0]} {contact_info[1]} ')
        print(f'Phobne Number : {contact_info[2]}')
        print(f'Email : {contact_info[3]}')
    else: 
        print('no contact infrmation fourn for this last name. ')

def main():
    filename = r'C:\Users\Labinfo22\Documents\Manfred Salas\D.csv' # change this to your csv file locaton 
    
    contacts = load_contacts(filename)
    last_name = input('Please enter a last name to look up: ').strip() # . strip () is used to delate any whites
    contact_info = contacts.get(last_name)

    display_contact_info(contact_info)

if __name__ == '__main__':
    main()