# Insertion sort is a simple sorting algorithm that is relatively efficient for 
# small lists and mostly sorted lists, and is often used as part of more 
# sophisticated algorithms. It works by taking elements from the list one 
# by one and inserting them in their correct position into a new sorted list.
# In arrays, the new list and the remaining elements can share the array's space, 
# but insertion is expensive, requiring shifting all following elements over by 
# one. Shellsort (see below) is a variant of insertion sort that is more efficient
# for larger lists.

def insertion(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr

# The running time of the algorithm 
import timeit
runningtime = timeit.timeit('insertion([i for i in reversed(range(10000))])',\
                    setup="from __main__ import insertion", number=1)
# runningtime = 11.9 sec