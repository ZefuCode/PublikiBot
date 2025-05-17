# ---------- LISTA ----------
mi_lista = []

def listas_demo():
    while True:
        print("\n--- LISTA ---")
        print("Lista actual:", mi_lista)
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            elem = input("Elemento a agregar: ")
            mi_lista.append(elem)
        elif opcion == "2":
            elem = input("Elemento a eliminar: ")
            if elem in mi_lista:
                mi_lista.remove(elem)
            else:
                print("No se encontró el elemento.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# ---------- PILA y COLA ----------
pila = []
cola = []

def pila_cola_demo():
    while True:
        print("\n--- PILA Y COLA ---")
        print("Pila:", pila)
        print("Cola:", cola)
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Encolar")
        print("4. Desencolar")
        print("5. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            elem = input("Elemento a apilar: ")
            pila.append(elem)
        elif opcion == "2":
            if pila:
                print("Elemento desapilado:", pila.pop())
            else:
                print("La pila está vacía.")
        elif opcion == "3":
            elem = input("Elemento a encolar: ")
            cola.append(elem)
        elif opcion == "4":
            if cola:
                print("Elemento desencolado:", cola[0])
                cola.pop(0)
            else:
                print("La cola está vacía.")
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

# ---------- ÁRBOL BINARIO ----------
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_rec(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_rec(nodo.der, valor)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorden(nodo.der)

arbol = Arbol()

def arbol_demo():
    while True:
        print("\n--- ÁRBOL BINARIO ---")
        print("1. Insertar número")
        print("2. Mostrar inorden")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            try:
                num = int(input("Ingresa un número: "))
                arbol.insertar(num)
            except ValueError:
                print("Solo se permiten números enteros.")
        elif opcion == "2":
            print("Recorrido inorden:", end=" ")
            arbol.inorden(arbol.raiz)
            print()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# ---------- DICCIONARIO ----------
diccionario = {}

def diccionario_demo():
    while True:
        print("\n--- DICCIONARIO ---")
        print("Diccionario actual:", diccionario)
        print("1. Agregar clave-valor")
        print("2. Consultar clave")
        print("3. Eliminar clave")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            clave = input("Clave: ")
            valor = input("Valor: ")
            diccionario[clave] = valor
        elif opcion == "2":
            clave = input("Clave a consultar: ")
            if clave in diccionario:
                print("Valor:", diccionario[clave])
            else:
                print("Clave no encontrada.")
        elif opcion == "3":
            clave = input("Clave a eliminar: ")
            if clave in diccionario:
                del diccionario[clave]
            else:
                print("Clave no encontrada.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# ---------- MENÚ PRINCIPAL ----------
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Lista")
    print("2. Pila y Cola")
    print("3. Árbol Binario")
    print("4. Diccionario")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listas_demo()
        elif opcion == "2":
            pila_cola_demo()
        elif opcion == "3":
            arbol_demo()
        elif opcion == "4":
            diccionario_demo()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

main()
