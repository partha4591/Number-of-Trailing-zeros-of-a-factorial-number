# Here in this program...we are going to find number of trailing zeroes of a factorial number. Sometimes it becomes difficult to find factorial of a large number.In which it produces errors. It can be resolved


def factorial(num):
    for i in range(num, 0, -1):
        if i == 1 or i == 0:
            return 1

        else:
            fact = num * factorial(num - 1)
            return fact


def trailing_zeros(factorial_number):
    print(factorial(factorial_number))
    count = 0
    i = 5
    while factorial_number // i != 0:
        count = count + int(factorial_number / i)
        i = i * 5

    return count


number = int(input("Enter the number: "))
print(f"number of trailing zeros: {trailing_zeros(number)}")
