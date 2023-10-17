capacidad = 10
elementos = [-1] * capacidad
tope = -1

print("Teclea elemento de la pila (termina con -1)")

CLAVE = -1

while True:
    entrada = input()
    
    if entrada.isdigit():
        x = int(entrada)
        
        if tope < capacidad - 1:
            tope += 1
            elementos[tope] = x
        else:
            print("Excepción: Pila llena")
            break
    else:
        print("Excepción: Entrada no válida")

if tope >= 0:
    print("Elementos de la Pila:", end="")
    while tope >= 0:
        x = elementos[tope]
        tope -= 1
        print(x, end=" ")
    print()
else:
    print("Pila vacía")
