#-------------------------------------------------------FALTA PUSHEAR ESTO
# 4) Buscar carácter específico 
def pedir_caracter() -> str:
    """Función que pide y valida el ingreso de un caracter

    Returns:
        str: Caracter solicitado
    """
    
    while True:
        caracter = input("Ingrese un caracter para buscar: ")
        
        if len(caracter) != 1:
            print("ERROR INGRESE UN SOLO CARACTER")
        else:
            break

    return caracter
    
#Recorro la cadena con un índice para poder conocer cada posición. Comparo cada carácter con el buscado,
#y si coincide incremento un contador y registro la posición donde ocurrió.

def buscar_caracter(cadena: str, caracter: str) -> None:
    """Busca un carácter dentro de una cadena y muestra cuántas veces aparece
    junto con las posiciones en las que se encuentra.

    Args:
        cadena (str): cadena donde se realiza la búsqueda.
        caracter (str): carácter a buscar dentro de la cadena.
    """
    contador_caracter = 0
    posiciones = ""

    for i in range(len(cadena)): #recorro por índice para acceder a posición y valor
        if cadena[i] == caracter: #comparo por posiciones con el caracter ingresado 
            contador_caracter += 1
            posiciones += str(i) + " "

    print(f"Aparece {contador_caracter} veces en posiciones: {posiciones}")

# 5)

