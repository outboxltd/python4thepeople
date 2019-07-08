for i in demo_list:
    # is_NOT_num = type(i) != int:
    if is_NOT_num in demo_list:
         demo_list.remove(is_NOT_num)

print(demo_list)