import os

# Python program to replace text in a file
x = "15"
y = "0 "
# file.txt should be replaced with
# the actual text file name
input_path = "C:\\Users\\Admin\\Desktop\\pics\\"
for fName in sorted(os.listdir(input_path)):
    if fName.endswith(".txt"):
        f = open(input_path + fName, "r")
        # each sentence becomes an element in the list l
        l = f.readlines()
        new_data = y + l[0][3:]
        f = open(input_path + fName, "w")
        f.write(new_data)
        print(new_data)