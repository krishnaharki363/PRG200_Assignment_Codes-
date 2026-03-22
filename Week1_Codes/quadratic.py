#Write a program to find the roots of a quadratic equation. Check all conditions for real roots, equal roots 
# and imaginary roots and display the roots. 
#Formula = b*b - 4*a*c/ 

import math 

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

d = b*b - 4*a*c

if a ==0:
    print("It is not a quadratic equation.")
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b _ math.sqrt(d)) / (2*a)
    print("Roots are real and different")
    print("Roots 1 =", r1)
    print("Root 2 =," r2)
elif d == 0:
    