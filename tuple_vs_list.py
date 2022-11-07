# tuple vs list

colors_list = ['red', 'pink', 'blue', 'yellow']
colors_tuple = ('red', 'pink', 'blue', 'yellow')

# replacing yellow with gray - list

colors_list[3] = 'gray'
print(colors_list)

# replacing yellow with gray - tuple

colors_tuple[3] = 'gray'
print(colors_tuple) # will not work, gives an error: 'tuple' object does not support item assignment

# Tuples defined by a comma. parenthesis makes it look neater

tuple_colors = 'red', 'pink', 'blue'
print(tuple_colors)

#for only one element in tuple you need to add comma at the end

my_tuple = (3,) 
