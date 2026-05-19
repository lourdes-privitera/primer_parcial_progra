
#valida la opcion elegida para que no falle el programa
def validar_entero(texto: str, valor_minimo:int, valor_maximo:int) -> bool:
    """Valida si un texto representa un número entero dentro de un rango.

    Args:
        texto (str): Cadena a validar.
        valor_minimo (int): Límite inferior permitido.
        valor_maximo (int): Límite superior permitido.

    Returns:
        bool: True si el texto es un entero dentro del rango, False en caso contrario.
    """
    retorno = False
    es_entero = True
        
    for c in texto: # Validar que todos los caracteres sean dígitos
        if not ("0" <= c <= "9"):
            es_entero = False
   
    if es_entero:  # Si es entero, validamos el rango numérico
        numero = int(texto)
        if valor_minimo <= numero <= valor_maximo:
            retorno = True
        else:
            print(f"ERROR: valor fuera de rango ({valor_minimo}/{valor_maximo}).")
    else:
        print("ERROR: se debe ingresar un número entero.")

    return retorno

#Permitir ingresar una contraseña.
def ingresar_contrasena() -> str:
    """Solicita y valida el ingreso de una contraseña.

    Returns:
        str: Contraseña ingresada.
    """
    aviso ="La contaseña debe tener minimo 8 caracteres, no puede iniciar con espacios y al menos debe contener una letra" 
    print(f"{aviso}")
    contrasena = input("Ingrese contraseña: ")
    
    while True:
        bandera_valida = True

        if validar_longitud_cadena(contrasena,8) == False:
            print("ERROR: La contaseña debe tener minimo 8 caracteres")   
            bandera_valida = False   
            
        if validar_inicio_espacio(contrasena) == False:
            print("ERROR: La contaseña no puede iniciar con espacios")        
            bandera_valida = False   
        if validar_letra(contrasena) == False:
            print("ERROR: La contaseña al menos debe contener una letra")        
            bandera_valida = False   
        if bandera_valida:
            break
        
        contrasena = input("Reingrese contraseña: ")
    return contrasena

#Validaciones obligatorias: 

#Utilizo y reutilizo (si es mayor a 8 no esta vacia)
def validar_longitud_cadena(cadena:str,minimo:int) -> bool:
    """Valida que una cadena tenga una longitud mínima.

    Args:
        cadena (str): Cadena a validar.
        minimo (int): Longitud mínima requerida.

    Returns:
        bool: True si cumple la longitud mínima.
    """

    retorno = False
    if len(cadena) >= minimo :
        retorno = True
    return retorno

#-no puede comenzar con espacios 
def validar_inicio_espacio(cadena:str) -> bool:
    """Valida que la cadena no comience con espacio.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si NO comienza con espacio.
    """
    bandera_inicio = False
    primer_caracter = cadena[0]
    codigo_ascii = ord(primer_caracter)
    if codigo_ascii != 32:
        bandera_inicio = True
    return bandera_inicio

#-debe contener al menos una letra
def validar_letra(cadena:str) -> bool:
    """Valida que la cadena contenga al menos una letra.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si contiene una letra.
    """
    
    bandera_letra = False
    for caracter in cadena:
        codigo_ascii = ord(caracter)
        if (65 <= codigo_ascii <= 90) or (97 <= codigo_ascii <= 122):
            bandera_letra = True
    return bandera_letra



    



