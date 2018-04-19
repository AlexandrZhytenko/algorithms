# countdown
def understand_recursion(number):
    print number
    if number <= 0:
        return "Stop working"
    understand_recursion(number - 1)

print understand_recursion(3)

# stack recursion (factorial)
def fact(number):
    print number
    if number == 1:
        return 1
    return number * fact(number - 1)

print fact(3)

def sum_items(arr):
    result = arr.pop(0)
    print result
    if len(arr) > 0:
        result = result + sum_items(arr)
    return result

print sum_items([1,2,3,4])