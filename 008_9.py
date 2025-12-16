# Numero palindromo, Leetcode N.9

def numeroPalindromo(numero:int):
    conversion = str(numero)
    arr_entrada = []

    for elemento in conversion:
        arr_entrada.append(elemento)

    reverse_arr = arr_entrada[::-1]

    if str(arr_entrada) == str(reverse_arr):
        return True
    else:
        return False

entrada = int(input("Coloca un numero: \n"))
call = numeroPalindromo(entrada)
print(call)
