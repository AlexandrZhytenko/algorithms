# Selection sort
# https://en.wikipedia.org/wiki/Selection_sort

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# or:
# find_smallest = arr.index(min(arr))

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

arr = [9,1,8,3,7,2]

from timeit import default_timer

start_timer = default_timer()
print "Result of selection_sort from {}: ".format(arr), selection_sort(arr)
end_timer = default_timer()
print "Time taken for execute selection_sort: ", end_timer - start_timer, "sec"

# Result of selection_sort from [9, 1, 8, 3, 7, 2]:  [1, 2, 3, 7, 8, 9]
# Time taken for execute selection_sort:  8.82679115863e-05 sec