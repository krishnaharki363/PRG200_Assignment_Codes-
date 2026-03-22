x = input("Enter a number or string: ")

rev = x[::-1]

if x == rev:
    print("Palindrome")
else:
    print("Not a palindrome")