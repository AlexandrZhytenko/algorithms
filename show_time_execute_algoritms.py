import math

def show_time_execute_algoritms(arr_len):
    for i in arr_len:
        # O(log n)
        print "For O(log n) where n={} time:".format(i), math.log(i, 2)/10.0, "sec"
        # O(n)
        print "For O(n) where n={} time:".format(i), i / 10.0, "sec"
        # O(n log n)
        print "For O(n log n) where n={} time:".format(i), i * math.log(i, 2)/10.0, "sec"
        # O(n**2)
        print "For O(n**2) where n={} time:".format(i), i ** 2 / 10.0, "sec"
        # O(n!)
        print "For O(n!) where n={} time:".format(i), math.factorial(i) / 10.0, "sec"

# arr_len = [16]
print show_time_execute_algoritms(arr_len)