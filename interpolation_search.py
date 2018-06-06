
def interpolation_search(input_list, target_element):
    # input_list = sorted(input_list)
    min_index = 0
    max_index = len(input_list)-1
    while (min_index <= max_index) and target_element >= input_list[min_index]\
            and target_element <= input_list[max_index]:
        mid_index = min_index + \
                    int(((float(max_index - min_index) / (input_list[max_index] - input_list[min_index])) \
                    * (target_element - input_list[min_index])))
        if input_list[mid_index] == target_element:
            return mid_index
        if input_list[mid_index] < target_element:
            min_index = mid_index + 1

if __name__ == "__main__":
    input_list = [2, 6, 11, 19, 27, 31, 45, 121]
    target_element = 11
    print interpolation_search(input_list, target_element)