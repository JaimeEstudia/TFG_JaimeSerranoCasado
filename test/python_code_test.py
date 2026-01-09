from typing import TypedDict

password = "jamon123"
print("Introduce la contraseña")
userinput = input()


def suma(a, b):
    return a + b


if password == userinput:
    print("Numeros para sumar:")
    a = input()
    b = input()
    print(suma(a, b))
else:
    print("Contraseña incorrecta")
