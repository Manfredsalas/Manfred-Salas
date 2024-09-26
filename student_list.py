# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
list_student = ["Emily Johnson", "Michael Smith", "Sarah Brown","David Williams", "Jessica Garcia", "James Miller", "Olivia Davis", "Daniel Rodriguez", "Sophia Martinez", "Ethan Hernandez"]
def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    #TODO HINT: Print each student in the 'students' list
    for element in list_student:
        print(element)
    print(f"_____________________________________")
    

# Add a new student to the list
def add_student():
    #TODO HINT: Ask the user for the student's name.
    Name = input('Enter the student name: ')
    #TODO Append the student's name to the 'students' list
    list_student.append(Name)
    #TODO display the updated list
    display_students()
    
    

# Remove a student from the list by name
def remove_student():
    #TODO HINT: Ask the user for the student's name to remove
    name_student = input('Enter the student name that you want to remove: ')
    #TODO Check if the student is in the list, then remove it
    if name_student in list_student:
        list_student.remove(name_student)
    #TODO If the student is not found, print an error message
    else:
        print('That name is not in the list. ')
    #TODO display the updated list
    display_students()


# remove a student from the end of the list
def pop_student():
    
    #TODO HINT: Remove the last student from the list
    laststudetn = list_student[-1]
    list_student.pop()
    #TODO If the list is not empty, display the name of the student removed
    print(f'You delete the name of {laststudetn}')

    #TODO If the list is empty, print a message saying there are no students left
    if len(list_student) == 0:
        print('Error this list is empty')

    #TODO display the updated list
    display_students()
    

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    name = input(' write the name of the student you want to update: ')
    newname = input('Write the name of new studet: ')
    #TODO Check if the student is in the list, then ask for the new name
    find = list_student.index(name)
    #TODO Update the student's name in the list
    list_student[find] = newname
    #TODO If the student is not found, print an error message
    if not newname:
        print('That name is not in the list. ')
    else:
        print('This name exist.')
    #TODO display the updated list
    display_students()

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        #TODO depending of the user choice option (1 - 5), call the correct function
        if choice == '5':
            break
        elif choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            pop_student()
        elif choice == '4':
            update_student()
menu()