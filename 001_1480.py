def runSum(array):
        runningSum = []
        suma = []

        for numero in array:
                suma.append(numero)
                newNumber = sum(suma)
                runningSum.append(newNumber)

        return runningSum

# Ejecuccion del codigo
nums = [1,2,3,4]
call = runSum(nums)
print(call)

# Salida esperada --> [1, 3, 6, 10]
