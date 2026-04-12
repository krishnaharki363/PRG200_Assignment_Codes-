my_list = [10, 20, 30]
#Accessing the individual elements in the list

print("Access: ", my_list[0])
print("Access: ", my_list[1])
print("Access: ", my_list[2])

my_list.append(40) #Adding the data in the list
print("Updated List: ", my_list)

with open ("list.txt", "w") as file:
    file.write(str(my_list))