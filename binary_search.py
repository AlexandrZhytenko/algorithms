def binary_search(arr, item):
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        middle = (start_index + end_index)/2
        guess = arr[middle]
        if guess == item:
            return middle
        elif guess > item:
            end_index = middle - 1
        else:
            start_index = middle + 1
    return None

my_arr = range(1, 1000001)
item = 500

from timeit import default_timer

start_timer = default_timer()
binary_search(my_arr, item)
end_timer = default_timer()

print "Result of binary search: ", binary_search(my_arr, item)
print "Time taken for binary search: ", end_timer - start_timer, "sec"

start_timer1 = default_timer()
for number in my_arr:
    if number == item:
        result_loop_search = my_arr.index(number)
end_timer1 = default_timer()

print "Result of loop search: ", result_loop_search
print "Time taken for loop search: ", end_timer1 - start_timer1, "sec"

print "Difference for time execution is ", \
    (end_timer - start_timer) - (end_timer1 - start_timer1), "sec"