num = int(input("Enter a large number: "))
count = 0

while num > 0:
    num = num // 10 #removes last number 
    count = count + 1 # each times digit is removed, count increases. 

print("Number of digits =", count)