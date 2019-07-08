def fun_number():
    print("please enter number")
    num = input()
    print("You entered the number: {0} ".format(num))
    list_4_the_num = []
    for x in num:
        list_4_the_num.append(x)
    print("The digits of this number are: {0}".format(list_4_the_num))
#   convert list to sum
    list_in_int = [int(i) for i in list_4_the_num]
    print(list_in_int)    
    the_sum = sum(list_in_int)
    print("the sum of it is : {0} ".format(the_sum))
fun_number()