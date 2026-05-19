from validaciones import contar_tipo_caracteres

from utilidades import calcular_porcentaje

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

# 5) Mostrar contraseña invertida 
#Recorro la cadena mediante índices para poder acceder a cada posición. 
#Después creo una nueva cadena agregando los caracteres en orden inverso al original.
def invertir_cadena(cadena:str) -> str:
    """Función que recorre la cadena desde el último índice hasta el primero,
    construyendo una nueva cadena en orden inverso.

    Args:
        cadena (str): cadena original a invertir.

    Returns:
        str: cadena con los caracteres en orden inverso.
    """
    cadena_invertida = ""

    for i in range (len(cadena)-1,-1,-1): #empieza en el último indice, termina en 0 (no se incluye) y va para atras
        cadena_invertida += cadena[i]

    return cadena_invertida

# 7)Verificar si es palíndromo 
#REUTILIZO LA FUNCION DE INVERTIR Y SOLO COMPARO ...
def verificar_palindromo(cadena:str) -> bool:
    """Función que comparando la cadena original con su versión invertida.

    Args:
        cadena (str): cadena a evaluar.

    Returns:
        bool: True si es palíndromo, False en caso contrario.
    """
    contrasena_invertida = invertir_cadena(cadena)

    if cadena == contrasena_invertida:
            retorno = True
    else:
            retorno =False
            
    return retorno

# 8)Ordenar caracteres de la contraseña 
#Utilizo un algoritmo de ordenamiento manual por comparación e intercambio de elementos.  (Selection Sort)
#comparo con todo a la derecha o izquierda
def ordenar_contrasena(cadena: str, orden: str) -> str:
    """Ordena los caracteres de una contraseña de forma ascendente o descendente
    utilizando un algoritmo de ordenamiento manual basado en comparación ASCII.

    Args:
        cadena (str): contraseña original a ordenar.
        orden (str): criterio de ordenamiento ("ascendente" o "descendente").

    Returns:
        str: contraseña con caracteres ordenados según el criterio indicado.
    """

    lista = []

    # convertir string a lista manualmente ya que los strings no se pueden intercambiar directamente
    for i in range(len(cadena)):
        lista += cadena[i]

    for izq in range(len(lista) - 1):
        for der in range(izq + 1, len(lista)):
            #ordenamiento por comparación
            if orden == "ascendente":
                if lista[izq] > lista[der]:  # comparación ASCII
                    aux = lista[izq]         # guardo temporal
                    lista[izq] = lista[der]  # intercambio
                    lista[der] = aux

            else:
                if lista[izq] < lista[der]:
                    aux = lista[izq]
                    lista[izq] = lista[der]
                    lista[der] = aux
    
    resultado = "" # nueva cadena
    for i in range(len(lista)):
        resultado += lista[i] # voy agregando la contraseña ordenada

    return resultado

# 6) Generar reporte estadístico 
def reporte_estadistico(cadena: str) -> None:
    """
    Muestra reporte estadístico de la contraseña.

    Muestra:
    - longitud total
    - porcentaje de letras
    - porcentaje de números
    - porcentaje de símbolos
    - cantidad de caracteres repetidos consecutivos

    Args:
        cadena (str): contraseña a analizar.
    """

    longitud_total = len(cadena)

    # reutilizo función ya creada
    cantidad_letras = contar_tipo_caracteres(cadena, "letra")
    cantidad_numeros = contar_tipo_caracteres(cadena, "numero")
    cantidad_simbolos = contar_tipo_caracteres(cadena, "simbolo")

    # cálculo porcentajes
    porcentaje_letras = calcular_porcentaje(cantidad_letras, longitud_total)
    porcentaje_numeros = calcular_porcentaje(cantidad_numeros, longitud_total)
    porcentaje_simbolos = calcular_porcentaje(cantidad_simbolos, longitud_total)

    # repetidos consecutivos
    repetidos_consecutivos = 0

    for i in range(1, len(cadena)):

        # comparo carácter actual con el anterior
        if cadena[i] == cadena[i - 1]:
            repetidos_consecutivos += 1

    # mostrar reporte
    print(f"Longitud total: {longitud_total}")
    print(f"Porcentaje letras: {porcentaje_letras}%")
    print(f"Porcentaje números: {porcentaje_numeros}%")
    print(f"Porcentaje símbolos: {porcentaje_simbolos}%")
    print(f"Cantidad de repetidos consecutivos: {repetidos_consecutivos}")

