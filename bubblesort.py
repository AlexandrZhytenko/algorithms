# bubblesort

def bubblesort(input_list, not_sorted=True):
    while not_sorted:
        not_sorted = False
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                temp = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = temp
                not_sorted = True
    return input_list

if __name__ == "__main__":
    input_list = [3, 5, 2, 1, 8, 9, 15]
    print bubblesort(input_list)