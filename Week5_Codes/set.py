my_set = { 80, 90, 100}

#Accessing using loop
for item in my_set:
    print("Item: ", item)

#Adding 110: 
my_set.add(110)
print("Updated Set:", my_set)

#Storing in txt file
with open("set.txt", "w") as file:
    file.write(str(my_set))