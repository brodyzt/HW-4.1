from Sort import Sort
from Person import PersonTrait
class Chair:

    counter = 0

    # loads chairs from save file
    @staticmethod
    def load_from_file():
        pass

    # saves current chairs to save file
    @staticmethod
    def save_to_file():
        pass

    # initializes the Chair object
    def __init__(self,person,next_chair=None):
        self.id = Chair.counter
        Chair.counter += 1
        self.person = person
        self.next_chair = next_chair

    # overrides the string output function for Chair object
    def __str__(self):
        try:
            return 'ID:{}, Next Chair:{}, Person:{}'.format(self.id,self.next_chair.id,self.person)
        except AttributeError:
            return 'ID:{}, Next Chair:none, Person:{}'.format(self.id,self.person)

class ChairStructure:

    # creates new ChairStructure object using list of Chairs
    @staticmethod
    def build_from_list_of_chairs(chair_list):
        new_structure = ChairStructure(chair_list)
        for x in range(len(chair_list) - 1):
            new_structure.structure[x].next_chair = new_structure.structure[x+1]
        new_structure.structure[len(chair_list)-1].next_chair = new_structure.structure[0]
        return new_structure

    # creates new ChairStructure object using list of people
    @staticmethod
    def build_from_list_of_people(list):
        chair_list = []
        for person in list:
            chair_list.append(Chair(person))
        return ChairStructure.build_from_list_of_chairs(chair_list)

    # initializes ChairStructure object
    def __init__(self, structure=[]):
        self.structure = structure

    # overrides string output of class
    def __str__(self):
        temp_str = ''
        for chair in self.structure:
            temp_str = temp_str + str(chair) + '\n'
        return temp_str

    # sorts the structure by personality rating of people in chairs
    def sort_by_personality_rating(self):
        self = ChairStructure.build_from_list_of_chairs(Sort.bubble_sort(self.structure, [chair.person.personality_rating for chair in self.structure]))

    def contains_person_with_trait(self, trait_type, trait_value):
        for chair in self.structure:
            if chair.person.data()[PersonTrait.dic[trait_type]] == trait_value:
                return True



        else: return False

    def remove_person_with_trait(self, trait_type, trait_value):
        for x in range(len(self.structure)):
            if self.structure[x].person.data()[PersonTrait.dic[trait_type]] == trait_value:
                self.structure.pop(x)
                break

        self = ChairStructure.build_from_list_of_chairs([chair for chair in self.structure])

    def add_person(self, new_person):
        temp_person_list = [chair.person for chair in self.structure]
        temp_person_list.append(new_person)
        return ChairStructure.build_from_list_of_people(temp_person_list)