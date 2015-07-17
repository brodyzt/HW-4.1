class Sort:

    # sorts list using bubble sort
    def bubble_sort(base_list, value_list):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for x in range(len(base_list) - 1):
                if(value_list[x] > value_list[x+1]):
                    base_list[x],base_list[x+1]=base_list[x+1],base_list[x]
                    value_list[x],value_list[x+1]=value_list[x+1],value_list[x]
                    is_sorted = False
        return base_list

    # sorts list using selection sort
    def selection_sort(base_list, value_list):
        for x in range(0, len(base_list) - 1):
            temp_lowest = value_list[x]
            temp_lowest_location = x
            for y in range(x + 1, len(base_list)):
                if value_list[y] < temp_lowest:
                    temp_lowest = value_list[y]
                    temp_lowest_location = y
            base_list[x],base_list[temp_lowest_location]=base_list[temp_lowest_location],base_list[x]
            value_list[x],value_list[temp_lowest_location]=value_list[temp_lowest_location],value_list[x]
        return base_list

    # sorts list using insertion sort
    def insertion_sort(base_list, value_list): # fix this
        temp_list = []
        list_length = len(base_list)
        for x in range(list_length):
            min = value_list[0]
            min_loc = 0
            for y in range(1, len(base_list)):
                if value_list[y] < value_list[min_loc]:
                    min = value_list[y]
                    min_loc = y
            temp_list.append(base_list[min_loc])
            base_list.pop(min_loc)
            value_list.pop(min_loc)
        return temp_list

    # sorts list using merge sort
    def merge_sort_data(base_list, value_list):
        if len(list) == 1:
            return [base_list, value_list]
        else:
            middle = len(base_list) // 2
            left_data = Sort.merge_sort_data(base_list[:middle], value_list[:middle])
            left_base = left_data[0]
            left_value = left_data[1]
            right_data = Sort.merge_sort_data(base_list[middle:len(list)],value_list[middle:len(list)])
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
            return [base_list, value_list]

    # removes accessory data from data returned from Sort.merger_sort_data()
    def merge_sort(base_list, value_list):
        return Sort.merge_sort_data(base_list, value_list)[0]

    # sorts list using radix_sort
    def radix_sort(list):
        pass

    # sorts list using quick_sort
    def quick_sort(list):
        pass