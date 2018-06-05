# countdown
def understand_recursion(number):
    print number
    if number <= 0:
        return "Stop working"
    understand_recursion(number - 1)

# stack recursion (factorial)
def fact(number):
    print number
    if number == 1:
        return 1
    return number * fact(number - 1)

# find sum items in list
def sum_items(arr):
    result = arr.pop(0)
    if len(arr) > 0:
        result = result + sum_items(arr)
    return result

if __name__ == "__main__":
    print sum_items([3, 5, 2, 1, 8, 9, 15])