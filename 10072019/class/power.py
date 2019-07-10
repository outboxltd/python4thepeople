def power(n,y):
    if y == 0:
        return 1
    else:
        resule = n * power(n,y-1)
        return resule
        
 
 

print(power(9,2))