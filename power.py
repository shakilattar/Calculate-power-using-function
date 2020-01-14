# Calculating power using function
number = int(input("Enter any Positive number = "))
exponent = int(input("Enter Exponent = "))


def power1(num):
    power = 1
    for i in range(1, exponent+1):
        power = power * num
    return power


result = power1(number)
print("The result is= ", result)




