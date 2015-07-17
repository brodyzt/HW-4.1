from Person import Person
from ChairStructure import Chair,ChairStructure

people = Person.load_from_file()
my_structure = ChairStructure.build_from_list_of_people(people)
print(my_structure)