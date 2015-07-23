from Sort import Sort
from Person import PersonTrait


class Chair:

    counter = 0

    # initializes the Chair object
    def __init__(self, person, next_chair=None, previous_chair = None):
        self.id = Chair.counter
        Chair.counter += 1
        self.person = person
        self.next_chair = next_chair
        self.previous_chair = previous_chair

    # overrides the string output function for Chair object
    def __str__(self):
        try:
            return 'ID:{}, Next Chair:{}, Person:{}'.format(self.id, self.next_chair.id, self.person)
        except AttributeError:
            return 'ID:{}, Next Chair:none, Person:{}'.format(self.id, self.person)

    # recursive function to return list of all chairs in structure
    def rest_of_list(self):
        if not self.next_chair:
            return [self]
        else:
            list = [self]
            list.extend(self.next_chair.rest_of_list())
            return list


class ChairStructure:

    # creates new ChairStructure object using list of Chairs
    @staticmethod
    def build_from_list_of_chairs(chair_list):
        new_structure = ChairStructure()
        new_structure.first_chair = chair_list[0]
        new_structure.last_chair = chair_list[1]
        new_structure.first_chair.next_chair = new_structure.last_chair
        new_structure.first_chair.previous_chair = None
        new_structure.last_chair.previous_chair = new_structure.first_chair
        new_structure.last_chair.next_chair = None

        for x in range(2,len(chair_list)):
            new_structure.add_chair(chair_list[x])
        return new_structure

    # creates new ChairStructure object using list of people
    @staticmethod
    def build_from_list_of_people(list):
        chair_list = []
        for person in list:
            chair_list.append(Chair(person))
        return ChairStructure.build_from_list_of_chairs(chair_list)

    # initializes ChairStructure object
    def __init__(self):
        self.first_chair = None
        self.last_chair = None

    # overrides string output of class
    def __str__(self):
        temp_str = ''
        for chair in self.chair_list():
            temp_str = temp_str + str(chair) + '\n'
        return temp_str

    # returns a list of all chairs in structure
    def chair_list(self):
        return self.first_chair.rest_of_list()

    # sorts the structure by personality rating of people in chairs
    def sort(self, trait, sort_method):
        chair_list = self.chair_list()
        person_data_list = [chair.person.data()[PersonTrait.dic[trait]] for chair in self.chair_list()]
        sorted_chair_list = sort_method(chair_list, person_data_list)
        temp = ChairStructure.build_from_list_of_chairs(sorted_chair_list)
        return temp

    # determines whether structure contains specified person
    def contains_person_with_trait(self, trait_type, trait_value):
        for chair in self.chair_list():
            if chair.person.data()[PersonTrait.dic[trait_type]] == trait_value:
                return True
        else:
            return False

    # removes specified person from structure
    def remove_person_with_trait(self, trait_type, trait_value):
        current_chair = self.first_chair
        while current_chair:
            if current_chair.person.data()[PersonTrait.dic[trait_type]] == trait_value:
                if current_chair.next_chair and current_chair.previous_chair:
                    current_chair.previous_chair.next_chair = current_chair.next_chair
                    current_chair.next_chair.previous_chair = current_chair.previous_chair
                    current_chair = current_chair.next_chair
                elif current_chair.next_chair:
                    self.first_chair = current_chair.next_chair
                    self.first_chair.previous_chair = None
                    current_chair = None
                elif current_chair.previous_chair:
                    self.last_chair = current_chair.previous_chair
                    self.last_chair.next_chair = None
                    current_chair = None
            else:
                current_chair = current_chair.next_chair

    # adds person to structure
    def add_person(self, new_person):
        temp_person_list = [chair.person for chair in self.chair_list()]
        temp_person_list.append(new_person)
        return ChairStructure.build_from_list_of_people(temp_person_list)

    # adds chair to structure
    def add_chair(self, input_chair):
        self.last_chair.next_chair = input_chair
        input_chair.previous_chair = self.last_chair
        self.last_chair = input_chair
        self.last_chair.next_chair = None