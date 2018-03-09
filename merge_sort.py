# merge sort(also commonly spelled mergesort) is an efficient, general - purpose, comparison - based
# sorting algorithm. Most implementations produce a stable sort, which means that the implementation
# preserves the input order of equal elements in the sorted output.

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    middle_of_arr = len(arr) / 2
    left = arr[0:middle_of_arr]
    right = arr[middle_of_arr:]
    left_side = merge_sort(left)
    right_side = merge_sort(right)
    return merge(left_side, right_side)

def merge(left_side, right_side):
    result = []
    while len(left_side) > 0 or len(right_side) > 0:
        if len(left_side) > 0 and len(right_side) > 0:
            if left_side[0] <= right_side[0]:
                result.append(left_side.pop(0))
            else:
                result.append(right_side.pop(0))
        elif len(left_side) > 0:
            result.append(left_side.pop(0))
        elif len(right_side) > 0:
            result.append(right_side.pop(0))
    return result

arr = [6, 5, 4, 3, 2, 1]
print merge_sort(arr)