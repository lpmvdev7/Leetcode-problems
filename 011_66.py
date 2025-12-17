# Leetcode numero 66. Plus One

def plusOne(digits):
        delimitador = ""
        string_map = map(str, digits)
        number_string = delimitador.join(string_map)
        suma = int(number_string) + 1

        suma_string = str(suma)
        suma_arr = []

        for n in suma_string:
            suma_arr.append(int(n))
        
        return suma_arr


digits = [4,3,2,1]

call = plusOne(digits)
print(call)
