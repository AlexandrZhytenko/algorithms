
def counting_sort(input_list):
    max_value = max(input_list) + 1
    counts = [0] * max_value
    for i in input_list:
        counts[i] += 1
    index = 0
    for i in range(max_value):
        for j in range(counts[i]):
            input_list[index] = i
            index += 1
    return input_list

if __name__ == "__main__":
    input_list = [3, 5, 2, 1, 8, 9, 15, 15, 1, 2, 3, 16]
    print counting_sort(input_list)