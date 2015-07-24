from Sort import Sort
from Person import PersonTrait
from copy import deepcopy


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
            return "Chair ID:{}, Next Chair's ID:{}, Person:{}".format(self.id, self.next_chair.id, self.person)
        except AttributeError:
            return "Chair ID:{}, Next Chair's ID:none, Person:{}".format(self.id, self.person)

    # recursive function to return list of all chairs in structure
    def rest_of_list(self):
        if not self.next_chair:
            return [self]
        else:
            list = [self]
            list.extend(self.next_chair.rest_of_list())
            return list

    def is_last_chair(self):
        return not self.next_chair

    def is_first_chair(self):
        return not self.previous_chair

    def is_middle_chair(self):
        return not self.is_first_chair() and not self.is_last_chair()


class ChairStructure:

    # creates new ChairStructure object using list of Chairs
    @staticmethod
    def build_from_list_of_chairs(chair_list):
        new_structure = ChairStructure()
        for x in range(0,len(chair_list)):
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
        self.length = 0

    # overrides string output of class
    def __str__(self):
        if self.length == 0:
            return 'Empty Chair Structure'
        else:
            temp_str = 'Length:{}, First Chair ID:{}, Last Chair ID:{}\n'.format(self.length, self.first_chair.id, self.last_chair.id)
            for chair in self.chair_list():
                temp_str = temp_str + str(chair) + '\n'
        return temp_str

    def get_length(self):
        len = 0
        if self.first_chair:
            len += 1
            temp_chair = self.first_chair
            while temp_chair:
                temp_chair = temp_chair.next_chair
                len +=1
        return len

    # returns a list of all chairs in structure
    def chair_list(self):
        return self.first_chair.rest_of_list()

    # sorts the structure by personality rating of people in chairs
    def sort(self, trait, sort_method):
        return sort_method(self, trait)

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
            if current_chair.person.data(trait_type) == trait_value:
                self.remove_chair(current_chair)
            current_chair = current_chair.next_chair

    # adds person to structure
    def add_person(self, new_person):
        self.add_chair(Chair(person=new_person))

    # adds chair to structure
    def add_chair(self, input_chair):
        input_chair.next_chair = None
        input_chair.previous_chair = None
        self.length += 1
        if not self.first_chair and not self.last_chair:
            self.first_chair = input_chair
            self.last_chair = input_chair
        elif not self.last_chair:
            self.last_chair = input_chair
            self.first_chair.next_chair = self.last_chair
            self.last_chair.previous_chair = self.first_chair
        else:
            self.last_chair.next_chair = input_chair
            input_chair.previous_chair = self.last_chair
            self.last_chair = input_chair
            self.last_chair.next_chair = None


    # adds new chair after the original chair specified in the structure
    def add_chair_after_chair(self, new_chair, orig_chair):
        new_chair.next_chair, new_chair.previous_chair = None, None
        self.length += 1
        if orig_chair.is_last_chair():
            self.last_chair.next_chair = new_chair
            new_chair.previous_chair = self.last_chair
            self.last_chair = new_chair
        else:
            new_chair.next_chair = orig_chair.next_chair
            new_chair.previous_chair = orig_chair
            orig_chair.next_chair.previous_chair = new_chair
            orig_chair.next_chair = new_chair

    # adds new chair after the original chair specified in the structure
    def add_chair_before_chair(self, new_chair, orig_chair):
        new_chair.next_chair, new_chair.previous_chair = None, None
        self.length += 1
        if orig_chair.is_first_chair():
            self.first_chair.previous_chair = new_chair
            new_chair.next_chair = self.first_chair
            self.first_chair = new_chair
        else:
            new_chair.previous_chair = orig_chair.previous_chair
            new_chair.next_chair = orig_chair
            orig_chair.previous_chair.next_chair = new_chair
            orig_chair.previous_chair = new_chair

    # removes chair from structure
    def remove_chair(self, input_chair):
        self.length -= 1
        if input_chair.previous_chair and input_chair.next_chair:
            input_chair.previous_chair.next_chair = input_chair.next_chair
            input_chair.next_chair.previous_chair = input_chair.previous_chair
        elif input_chair.previous_chair:
            input_chair.previous_chair.next_chair = None
            self.last_chair = input_chair.previous_chair
        elif input_chair.next_chair:
            input_chair.next_chair.previous_chair = None
            self.first_chair = input_chair.next_chair
        else:
            self.first_chair = None
            self.last_chair = None

    def chairs_before_and_including_index(self, input_index):
            input_chair = self.first_chair
            for _ in range(input_index - 1):
                input_chair = input_chair.next_chair

            temp_next = input_chair.next_chair
            input_chair.next_chair = None
            temp_last = self.last_chair
            self.last_chair = input_chair
            temp_length = self.length
            self.length = input_index + 1
            temp_structure = deepcopy(self)
            self.length = temp_length
            self.last_chair = temp_last
            input_chair.next_chair = temp_next
            return temp_structure

    def chairs_after_index(self, input_index):
            if input_index == self.length - 1:
                return ChairStructure()
            else:
                input_chair = self.first_chair
                for _ in range(input_index - 1):
                    input_chair = input_chair.next_chair

                input_chair.next_chair.previous_chair = None
                first_chair = self.first_chair
                self.first_chair = input_chair.next_chair
                temp_length = self.length
                self.length = self.length - (input_index + 1)
                temp_structure = deepcopy(self)
                self.length = temp_length
                self.first_chair = first_chair
                input_chair.next_chair.previous_chair = input_chair
                return temp_structure

    def remove_first_chair(self):
        if self.length == 1:
            self.__init__()
        else:
            self.first_chair = self.first_chair.next_chair
            self.first_chair.previous_chair = None
            self.length -= 1

