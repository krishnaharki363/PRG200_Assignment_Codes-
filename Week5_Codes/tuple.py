my_tuple = (10, 20, 30, 40, 50)

#Accessing the elements 
print("Access: ", my_tuple[0])
print("Access: ", my_tuple[1])
print("Access: ", my_tuple[2])
print("Access: ", my_tuple[3])
print("Access: ", my_tuple[4])

#Adding new elements or simply say (Creating new tuple)
my_tuple = my_tuple +(60,)
print("Updated Tuple: ", my_tuple)

with open("Tuple.txt", "w") as file:
    file.write(str(my_tuple))