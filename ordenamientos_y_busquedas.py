import random

def Menu():
    arr = [4, 1, 2, 3, 5]

    print("Arreglo inicial:", arr)

    while True:
        try:
            print("\nMenu")
            print("1. Ordenar arreglo")
            print("2. Buscar en el arreglo")
            print("3. Salir")

            choice = int(input("Opcion: "))

            if choice == 1:
                print("\nMetodos de ordenamiento:")
                print("1. Bubble Sort")
                print("2. Quick Sort")
                print("3. Merge Sort")

                metodo = int(input("Opcion: "))

                if metodo == 1:
                    Bubblesort(arr)
                elif metodo == 2:
                    arr = quicksort(arr)
                elif metodo == 3:
                    arr = mergesort(arr)
                else:
                    print("Metodo invalido")
                    continue

                print("Arreglo ordenado:", arr)

            elif choice == 2:
                if arr != sorted(arr):
                    print("El arreglo no esta ordenado. Ordenalo primero.")
                    continue

                buscar = int(input("Numero a buscar: "))

                pos = busqueda_lineal(arr, buscar)

                if pos != -1:
                    print(f"Encontrado en la posicion {pos}")
                else:
                    print("Numero no encontrado")

            elif choice == 3:
                print("Saliendo del programa...")
                break

            else:
                print("Opcion invalida")

        except ValueError:
            print("Error: Debes ingresar un numero entero")

        except Exception as e:
            print("Error inesperado:", e)


"""ordenamientos"""
#------------------------------------------------------------
def Bubblesort(arr):
    n = len(arr)
    for i in range (n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#-------------------------------------------------------------
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)
#------------------------------------------------------------
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mitad = len(arr) // 2
    izquierda = mergesort(arr[:mitad])
    derecha = mergesort(arr[mitad:])

    return merge(izquierda, derecha)


def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
#-------------------------------------------------------
"""busquedas"""
def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

#-------------------------------------------------------
def busqueda_binaria(arr, objetivo):
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1
#-----------------------------------------------------------
def busqueda_interpolacion(arr, objetivo):
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin and objetivo >= arr[inicio] and objetivo <= arr[fin]:
        if inicio == fin:
            if arr[inicio] == objetivo:
                return inicio
            return -1

        pos = inicio + ((objetivo - arr[inicio]) * (fin - inicio) //
                         (arr[fin] - arr[inicio]))

        if arr[pos] == objetivo:
            return pos
        elif arr[pos] < objetivo:
            inicio = pos + 1
        else:
            fin = pos - 1

    return -1
#---------------------------------------------------------------------------

def busqueda_aleatoria(arr, objetivo):
    intentos = 0
    max_intentos = len(arr)

    while intentos < max_intentos:
        i = random.randint(0, len(arr) - 1)
        if arr[i] == objetivo:
            return i
        intentos += 1

    return -1

Menu();