from Person import Person
from ChairStructure import ChairStructure, Chair
from Exceptions import SelectionError
from Sort import Sort
from BinarySearchTree import BinarySearchTree


def clear_screen():
    print('\n' * 30)

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
                if my_structure.contains_person_with_trait('id', person_id):
                    my_structure.remove_person_with_trait('id', person_id)
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
        temp_structure = [chair for chair in my_structure.chair_list() if chair.person.name == person_name]
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
            if not my_structure.contains_person_with_trait('personality', int(person_rating)):
                print("You didn't enter a valid Personality Rating. Please try again.")
                person_rating = int(input("Personality Rating: "))
            else:
                break
        print('Select which person you would like to remove.\n')
        temp_structure = [chair for chair in my_structure.structure if chair.person.personality_rating == int(person_rating)]
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


def sort_people(input_structure):
    clear_screen()
    print('Which of the traits would you like to sort by?\n')
    print('1.ID\n2.Name\n3.Age\n4.Personality Rating\n')
    trait = input('Choice: ')
    while not trait in ['1','2','3','4']:
        print("You didn't choose a valid option. Please try again.")
        trait = input('Choice: ')

    clear_screen()
    print('\nWhich sorting method would you like to use?')
    if trait == '2':
        print('\n1.Bubble Sort\n2.Insertion Sort\n3.Quick Sort\n4.Merge Sort\n5.Selection Sort\n')
        sort_method = input('Choice: ')
        while sort_method not in ['1','2','3','4','5']:
            print("You didn't enter a valid option. Please try again.")
            sort_method = input('Choice: ')
    else:
        print('\n1.Bubble Sort\n2.Insertion Sort\n3.Quick Sort\n4.Merge Sort\n5.Selection Sort\n6.Radix Sort\n')
        sort_method = input('Choice: ')
        while sort_method not in ['1','2','3','4','5','6']:
            print("You didn't enter a valid option. Please try again.")
            sort_method = input('Choice: ')

    sort_method_list = [Sort.bubble_sort, Sort.insertion_sort, Sort.quick_sort, Sort.merge_sort, Sort.selection_sort, Sort.radix_sort]
    trait_list = ['id','name','age','personality']

    return input_structure.sort(trait_list[int(trait) - 1], sort_method_list[int(sort_method) - 1])


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
    personality_rating = input('What is the personality rating of the person (Int between 1-100): ')
    while True:
        try:
            personality_rating = int(personality_rating)
            while not (personality_rating >= 0 and personality_rating <= 100):
                print("You didn't enter a valid rating. Try again")
                personality_rating = int(input('What is the personality rating of the person (Int between 1-100): '))
            break
        except ValueError:
            print("You didn't enter a valid rating. Try again")
            personality_rating = input('What is the personality rating of the person (Int between 1-100): ')
    return Person(person_name,person_age,personality_rating)


def print_binary_tree(input_structure):
    clear_screen()
    print("What would you like the tree to be sorted by?\n")
    print("1.ID\n"
          "2.Name\n"
          "3.Age\n"
          "4.Personality Rating\n")
    choice = input('Choice: ')
    while not choice in ['1','2','3','4']:
        print("You didn't enter a valid choice. Please try again.")
        choice = input('Choice: ')
    my_tree = BinarySearchTree()
    for chair in input_structure.chair_list():
        my_tree.put(chair.person.data()[int(choice) - 1], chair)
    my_tree.print()


while running:
    print("What would you like to do\n")
    print("1.List Current Chair Setup\n"
          "2.Remove Person From Chair Setup\n"
          "3.Sort Setup\n"
          "4.Update Save File\n"
          "5.Add Person\n"
          "6.Print Binary Search Tree\n")
    selection = input("Choice: ")

    if selection == '1':
        print(my_structure)
        print('\nListed!!')
    elif selection == '2':
        remove_person()
        clear_screen()
        print('Removed!')
    elif selection == '3':
        my_structure = sort_people(my_structure)
        clear_screen()
        print('Sorted!!')
    elif selection == '4':
        Person.save_to_file([chair.person for chair in my_structure.chair_list()])
        clear_screen()
        print('Saved!!')
    elif selection == '5':
        new_person = build_new_person()
        new_chair = Chair(new_person)
        my_structure = my_structure.add_person(new_person)
        clear_screen()
        print('Added!!')
    elif selection == '6':
        print_binary_tree(my_structure)
    else:
        print("You didn't enter a valid answer. Please try again")

    print('\n' * 5)