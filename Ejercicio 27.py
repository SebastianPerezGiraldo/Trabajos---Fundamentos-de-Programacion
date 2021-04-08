num1 = int(input('Ingresar un número: '))
num2 = int(input('Ingresar un número: '))
num3 = int(input('Ingresar un número: '))
if num1<num2 and num1<num3:
    print(num1)
else:
    if num2<num3:
        print(num2)
    else:
        print(num3)
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)