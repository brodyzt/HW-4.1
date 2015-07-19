from enum import Enum
class Person:
    # counter to ensure Person IDs aren't reused
    counter = 0

    # class method to load people from save file
    @staticmethod
    def load_from_file():
        file = open('People','r')
        contents = file.readlines()
        person_list = []
        contents.pop(0)
        for line in contents:
            person_data = line.split(',')
            name = person_data[0]
            age = int(person_data[1])
            personality_rating = float(person_data[2])
            person_list.append(Person(name,age,personality_rating))
        file.close()
        return person_list

    # class method to save updates people list to file
    @staticmethod
    def save_to_file(person_list):
        file = open('People','r+')
        file.truncate(0)
        file.write('Name,Age,Personality_Rating\n')
        for person in person_list:
            file.write('{},{},{}\n'.format(person.name,person.age,person.personality_rating))
        file.close()

    # initializes person object
    def __init__(self, name, age, personality_rating):
        self.id = Person.counter
        Person.counter += 1
        self.name = name
        self.age = age
        self.personality_rating = personality_rating

    # overrides string output of person object
    def __str__(self):
        return 'ID:{}, Name:{}, Age:{}, Personality:{}'.format(self.id,self.name,self.age,self.personality_rating)

    def data(self):
        return [self.id,self.name,self.age,self.personality_rating]

class PersonTrait():
   dic =  {'id':0,
            'name':1,
            'age':2,
            'personality':3}

