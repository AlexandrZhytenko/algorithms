# countdown
def understand_recursion(number):
    print number
    if number <= 0:
        return "Stop working"
    understand_recursion(number - 1)

print understand_recursion(3)