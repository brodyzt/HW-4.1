from Person import Person
from ChairStructure import Chair,ChairStructure
from Sort import Sort
from Exceptions import SelectionError

people = Person.load_from_file()
my_structure = ChairStructure.build_from_list_of_people(people)

running = True

def remove_person():
    print('Which of the following traits would you like to search?\n')
    print("1.ID\n"
          "2.Name\n"
          "3.Age\n"
          "4.Personality Rating")
    selection = input('Choice')

    while True:
        try:
            if not selection in ['1','2','3','4']: raise SelectionError
        except SelectionError:
            print("You didn't enter a valid option. Please try again.\n")
            selection = input("Choice: ")

    if selection == '1':
        print('What is the ID of the person you want to remove.')
        person_id = input('ID: ')


    elif selection == '2':

    elif selection == '3':

    elif selection == '4':


while running:
    print("What would you like to do\n")
    print("1.List Current Chair Setup\n"
          "2.Remove Person From Chair Setup\n"
          "3.Sort Setup By Personality\n"
          "4.Update Save File\n")
    selection = input("Choice: ")

    if selection == '1':
        print(my_structure)
    elif selection == '2':
        remove_person()
        print('Removed!')
    elif selection == '3':
        my_structure.sort_by_personality_rating()
        print('Sorted!!')
    elif selection == '4':
        Person.save_to_file([chair.person for chair in my_structure.structure])
        print('Saved!!')
    else:
        print("You didn't enter a valid answer. Please try again")

    print('\n' * 5)