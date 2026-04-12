import csv 
my_dict = {"name": "Krish", "age": 20}
print("Access: ", my_dict["name"])
print("Access: ", my_dict["age"])

#Add
my_dict["city"] = "Kathmadu"
print("Updated Dictionary: ", my_dict)

with open("dictionary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    #Header
    writer.writerow(["Key", "Value"])

    #This is for data
    for key, value in my_dict.items():
        writer.writerow([key, value])
    
