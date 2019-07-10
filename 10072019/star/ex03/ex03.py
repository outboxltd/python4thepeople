
def Make_Fibonacci(n):
    if n == 100: return n
    # elif n == 1: return 1
    else:
        return Make_Fibonacci(n+1) 

print(Make_Fibonacci(1))




# fibo_array =[]
#     if len(fibo_array) == 100:
#         return 0
#     else:
#         start_num = 1
#         result = start_num +second_num
#         fibo_array.append(result)
#         return fibo_array
