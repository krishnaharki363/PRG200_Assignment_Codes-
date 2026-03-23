"""
An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
## Simple Definition
If a number has n digits, then:
Sum of (each digit ^ n) = the number itself
"""

num = int(input("Enter a number: "))
temp = num
power = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** power
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")