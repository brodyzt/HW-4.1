from Person import PersonTrait
import ChairStructure
from copy import deepcopy



def get_digit(int_input, digit):
    if not digit > len(str(int_input)):
        return int(str(int_input)[len(str(int_input)) - digit])
    else:
        return 0


class Sort:

    # sorts list using bubble sort
    @staticmethod
    def bubble_sort(input_structure, input_trait):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            current_chair = input_structure.first_chair
            while current_chair.next_chair:
                if current_chair.person.data(input_trait) > current_chair.next_chair.person.data(input_trait):
                    current_chair.person, current_chair.next_chair.person = current_chair.next_chair.person, current_chair.person
                    is_sorted = False
                current_chair = current_chair.next_chair
        return input_structure

    # sorts list using selection sort
    @staticmethod
    def selection_sort(input_structure, input_trait):
        chair_to_replace = input_structure.first_chair
        while chair_to_replace.next_chair:
            current_chair = chair_to_replace.next_chair
            temp_lowest = current_chair
            while current_chair:
                if current_chair.person.data(input_trait) < temp_lowest.person.data(input_trait):
                    temp_lowest = current_chair
                current_chair = current_chair.next_chair
            chair_to_replace.person, temp_lowest.person = temp_lowest.person, chair_to_replace.person
            chair_to_replace = chair_to_replace.next_chair
        return input_structure

    # sorts list using insertion sort ---- fix
    @staticmethod
    def insertion_sort(input_structure, input_trait):
        input_structure = deepcopy(input_structure)
        current_chair = input_structure.first_chair.next_chair
        counter = 1
        while current_chair:
            temp_chair = input_structure.first_chair
            input_structure.remove_chair(current_chair)
            the_next_chair = current_chair.next_chair
            for y in range(counter):
                if current_chair.person.data(input_trait) <= temp_chair.person.data(input_trait):
                        input_structure.add_chair_before_chair(current_chair, temp_chair)
                        break
                if temp_chair.next_chair:
                    temp_chair = temp_chair.next_chair
            else:
                input_structure.add_chair_after_chair(current_chair, temp_chair)
            current_chair = the_next_chair
            counter += 1
        return input_structure

    def merge_sort_data(base_list, value_list):
        if not len(base_list) > 1:
            return [base_list, value_list]
        middle = len(value_list) // 2
        left_data = Sort.merge_sort_data(base_list[:middle], value_list[:middle])
        left_base = left_data[0]
        left_value = left_data[1]
        right_data = Sort.merge_sort_data(base_list[middle:len(base_list)], value_list[middle:len(value_list)])
        right_base = right_data[0]
        right_value = right_data[1]
        base_result = [0 for x in range(len(base_list))]
        value_result = [0 for x in range(len(base_list))]
        l_counter = 0
        r_counter = 0
        for m_counter in range(len(base_list)):
            if l_counter == len(left_base):
                base_result[m_counter] = right_base[r_counter]
                value_result[m_counter] = right_value[r_counter]
                r_counter += 1
            elif r_counter == len(right_base):
                base_result[m_counter] = left_base[l_counter]
                value_result[m_counter] = left_value[l_counter]
                l_counter += 1
            elif left_value[l_counter] < right_value[r_counter]:
                base_result[m_counter] = left_base[l_counter]
                value_result[m_counter] = left_value[l_counter]
                l_counter += 1
            else:
                base_result[m_counter] = right_base[r_counter]
                value_result[m_counter] = right_value[r_counter]
                r_counter += 1
        return [base_result, value_result]

    # removes accessory data from data returned by Sort.merger_sort_data()
    @staticmethod
    def merge_sort(input_structure, input_trait):
        base_list = input_structure.chair_list()
        value_list = [chair.person.data(input_trait) for chair in base_list]
        return ChairStructure.ChairStructure.build_from_list_of_chairs(Sort.merge_sort_data(base_list, value_list)[0])

    # sorts list using radix_sort
    @staticmethod
    def radix_sort(input_structure, input_trait):
        base_list = input_structure.chair_list()
        value_list = [chair.person.data(input_trait) for chair in base_list]
        max_length = max([len(str(num)) for num in value_list])
        for x in range(1,max_length+1):
            base_list = Sort.selection_sort(base_list, [get_digit(value_list[z], x) for z in range(len(value_list))])
            value_list = Sort.selection_sort(value_list, [get_digit(value_list[z], x) for z in range(len(value_list))])
        return ChairStructure.ChairStructure.build_from_list_of_chairs(base_list)

    # sorts list using quick_sort
    @staticmethod
    def quick_sort_data(base_list, value_list):

        if not len(base_list) > 1:
            return [base_list, value_list]
        else:
            less_base = []
            less_value = []
            equal_base = []
            equal_value = []
            greater_base = []
            greater_value = []
            pivot = value_list[len(base_list)//2]
            for x in range(len(base_list)):
                if value_list[x] < pivot:
                    less_base.append(base_list[x])
                    less_value.append(value_list[x])
                if value_list[x] == pivot:
                    equal_base.append(base_list[x])
                    equal_value.append(value_list[x])
                if value_list[x] > pivot:
                    greater_base.append(base_list[x])
                    greater_value.append(value_list[x])
            less = Sort.quick_sort_data(less_base, less_value)
            less_base = less[0]
            less_value = less[1]
            greater = Sort.quick_sort_data(greater_base, greater_value)
            greater_base = greater[0]
            greater_value = greater[1]
            return [less_base + equal_base + greater_base, less_value + equal_value + greater_value]

    # removes accessory data from data returned by Sort.quick_sort_data()
    @staticmethod
    def quick_sort(input_structure, input_trait):
        base_list = input_structure.chair_list()
        value_list = [chair.person.data(input_trait) for chair in base_list]
        return ChairStructure.ChairStructure.build_from_list_of_chairs(Sort.quick_sort_data(base_list, value_list)[0])
