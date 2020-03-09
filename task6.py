# 6. Given an integer. Print its tens digit.


# The solution for three digit number and less
integer = int(input("Enter a number: "))
tens_digit = int((integer % 100) / 10)
print(tens_digit)
