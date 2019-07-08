# Write a method that gets a list and returns the sum of it. Validate you’re only summing the numeric elements (not
# strings, dictionaries etc.)

demo_list = [1,2,3,8,"gilad"]

for x in demo_list:
    if type(x) != int:
        demo_list.remove(x)
print(demo_list)


list_in_int = [int(i) for i in demo_list]
print(list_in_int)    
the_sum = sum(list_in_int)
print("the sum of it is : {0} ".format(the_sum))
