from Person import Person, PersonTrait
from ChairStructure import Chair,ChairStructure
from Sort import Sort
from Exceptions import SelectionError

people = Person.load_from_file()
my_structure = ChairStructure.build_from_list_of_people(people)

running = True

def remove_person():
    print('\nWhich of the following traits would you like to search?\n')
    print("1.ID\n"
          "2.Name\n"
          "3.Age\n"
          "4.Personality Rating")
    print('\n')
    selection = input('Choice: ')
    while True:
        try:
            if not selection in ['1','2','3','4']: raise SelectionError
            else: break
        except SelectionError:
            print("You didn't enter a valid option. Please try again.\n")
            selection = input("Choice: ")

    print('\n')
    if selection == '1':
        print('What is the ID of the person you want to remove.')
        person_id = input('ID: ')
        while True:
            try:
                person_id = int(person_id)
                if my_structure.contains_person_with_trait('id',person_id):
                    my_structure.remove_person_with_trait('id',person_id)
                    break
                else:
                    print("You didn't enter a valid id. Please try again")
                    person_id = input("ID: ")

            except ValueError:
                break

    elif selection == '2':
        print('What is the Name of the person you want to remove.')
        person_name = input('Name: ')
        while True:
            if not my_structure.contains_person_with_trait('name', person_name):
                print("You didn't enter a valid name. Please try again.")
                person_name = input("Name: ")
            else:
                break
        print('Select which person you would like to remove.\n')
        temp_structure = [chair for chair in my_structure.structure if chair.person.name == person_name]
        for x in range(len(temp_structure)):
            print('{}. {}'.format(x+1,temp_structure[x]))
        final_choice = input('\nChoice: ')
        while True:
            try:
                final_choice = int(final_choice)
                if final_choice - 1 in range(len(temp_structure)):
                    my_structure.remove_person_with_trait('id', temp_structure[final_choice - 1].person.id)
                    break
                else:
                    raise SelectionError
            except SelectionError:
                print("You didn't enter a valid option. Please try again.")
                final_choice = input('Choice: ')
            except ValueError:
                print("You didn't enter a valid option. Please try again.")
                final_choice = input('Choice: ')

    elif selection == '3':
        print('What is the Age of the person you want to remove.')
        person_age = input('Age: ')
        while True:
            if not my_structure.contains_person_with_trait('age', int(person_age)):
                print("You didn't enter a valid age. Please try again.")
                person_age = input("Age: ")
            else:
                break
        print('Select which person you would like to remove.\n')
        temp_structure = [chair for chair in my_structure.structure if chair.person.age == int(person_age)]
        for x in range(len(temp_structure)):
            print('{}. {}'.format(x+1,temp_structure[x]))
        final_choice = input('\nChoice: ')
        while True:
            try:
                final_choice = int(final_choice)
                if final_choice - 1 in range(len(temp_structure)):
                    my_structure.remove_person_with_trait('id', temp_structure[final_choice - 1].person.id)
                    break
                else:
                    raise SelectionError
            except SelectionError:
                print("You didn't enter a valid option. Please try again.")
                final_choice = input('Choice: ')
            except ValueError:
                print("You didn't enter a valid option. Please try again.")
                final_choice = input('Choice: ')

    elif selection == '4':
        print('What is the Personality Rating of the person you want to remove.')
        person_rating = input('Personality Rating: ')
        while True:
            if not my_structure.contains_person_with_trait('personality', float(person_rating)):
                print("You didn't enter a valid Personality Rating. Please try again.")
                person_rating = float(input("Personality Rating: "))
            else:
                break
        print('Select which person you would like to remove.\n')
        temp_structure = [chair for chair in my_structure.structure if chair.person.personality_rating == float(person_rating)]
        for x in range(len(temp_structure)):
            print('{}. {}'.format(x+1,temp_structure[x]))
        final_choice = input('\nChoice: ')
        while True:
            try:
                final_choice = int(final_choice)
                if final_choice - 1 in range(len(temp_structure)):
                    my_structure.remove_person_with_trait('id', temp_structure[final_choice - 1].person.id)
                    break
                else:
                    raise SelectionError
            except SelectionError:
                print("You didn't enter a valid option. Please try again.")
                final_choice = input('Choice: ')
            except ValueError:
                print("You didn't enter a valid option. Please try again.")
                final_choice = input('Choice: ')

def build_new_person():
    person_name = input('What is the name of the person: ')
    person_age = input('What is the age of the person: ')
    while True:
        try:
            person_age = int(person_age)
            while not person_age > 0:
                print("You didn't enter a valid age. Try again")
                person_age = int(input('What is the age of the person: '))
            break
        except ValueError:
            print("You didn't enter a valid age. Try again")
            person_age = input('What is the age of the person: ')
    personality_rating = input('What is the personality rating of the person (Float between 1-10): ')
    while True:
        try:
            personality_rating = float(personality_rating)
            while not (personality_rating >= 0 and personality_rating <= 10):
                print("You didn't enter a valid rating. Try again")
                personality_rating = float(input('What is the personality rating of the person (Float between 1-10): '))
            break
        except ValueError:
            print("You didn't enter a valid rating. Try again")
            personality_rating = input('What is the personality rating of the person (Float between 1-10): ')
    return Person(person_name,person_age,personality_rating)

while running:
    print("What would you like to do\n")
    print("1.List Current Chair Setup\n"
          "2.Remove Person From Chair Setup\n"
          "3.Sort Setup By Personality\n"
          "4.Update Save File\n"
          "5.Add Person\n")
    selection = input("Choice: ")

    if selection == '1':
        print(my_structure)
    elif selection == '2':
        remove_person()
        print('Removed!')
    elif selection == '3':
        my_structure = my_structure.sort_by_personality_rating()
        print('Sorted!!')
    elif selection == '4':
        Person.save_to_file([chair.person for chair in my_structure.structure])
        print('Saved!!')
    elif selection == '5':
        my_structure = my_structure.add_person(build_new_person())
        print('Added!!')
    else:
        print("You didn't enter a valid answer. Please try again")

    print('\n' * 5)