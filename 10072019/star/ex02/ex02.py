def getMax(listo, x):
    if x == len(listo):
        return 0
    else:
        the_func = getMax(listo[1:],0)
        return the_func if the_func > listo[0] else listo[0]
     

print("the max is : " , getMax([10, 2, 300, 4, 5], 0))


# demo_array = [2,4,6,8,10.12,14]

# print(demo_array[1:])