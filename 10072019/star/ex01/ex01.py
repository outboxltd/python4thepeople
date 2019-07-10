def getSum(listo, n):
    if n == len(listo):
        return 0
    return listo[n] + getSum(listo, n+1)


print(getSum([1, 2, 3, 4, 5], 0))