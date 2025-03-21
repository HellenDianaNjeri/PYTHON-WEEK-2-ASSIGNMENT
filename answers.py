#empty list
my_list = []

#append 10,20,30,40 to my_list
for number in range(10,50,10):
    my_list.append(number)             
print(my_list)

#insert 15 at index 1
my_list.insert(1,15)
print(my_list)

# extend my_list with [50,60,70]  
list=[50,60,70]
my_list.extend(list)
print(my_list)

# remove the last element in my_list
my_list.pop(-1)
print(my_list)

# sort in ascending order
my_list.sort()
print(my_list) 

# find and print the index of 30 in my_list
my_list.index(30)
print(my_list.index(30))  

