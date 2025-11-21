num = int(input("Coloca un numero: "))

def numberOfSteps(num):
    steps = []
    while num != 0:
        if num % 2 == 0:
            num = num / 2
            steps.append(num)
        else:
            num = num - 1
            steps.append(num)
    return len(steps)

print(numberOfSteps(num))

