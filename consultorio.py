
def busca_arreglo(busca):#el peor ejemplo
    file = open ('palabras.txt')
    for item in file.read():
        if item in busca:
            print("Palabra encontrada")
            return ("Palabra encontrada en el arreglo")
        return ("No se encontro la palabra")
    #if busca in arreglo_palabras:
    #    print("tambien lo encontre")

def busca_in_file(busca):
    file =open ('palabras.txt','r')
    if busca in file.read():
        print("lo encontre con file read")
        return 1
    file = open('groserias.txt','r')
    if busca in file.read():
        print("\n\t\tlo encontre con file read")
        return 3
    file.close()
    return False


def busca_whit_file(busca):
    with open('palabras.txt') as file:
        data = True
        while data:
            data= file.readline()
            print(data)

texto = "Mi casa es green"

texto_analizar = texto.split()
for item in texto_analizar:
    print(f"analizando{item}")
    analisis = busca_arreglo(item)
    if not analisis:
        print("El texto contiene algo invalido")
    print(busca_in_file(item))