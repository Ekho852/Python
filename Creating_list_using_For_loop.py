# Creating list using For loop

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

my_list = []  # append -> insert(0,) reverses order of list

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)