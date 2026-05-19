from validaciones import * #SACAR ASTERISCO Y MENCIONAR A LAS FUNCIONES ESPECIFICAS QUE LLAMO ANTES DE PRESENTAR
#-------------------------------------------------------FALTA PUSHEAR ESTO
# 3) Contar tipos de caracteres
def mostrar_cantidad_caracteres(cadena:str) -> None:
    """Se ocupa de mostrar resultados, no devuelve nada

    Args:
        cadena (str): contraseña evaluada 
    """

    cantidad_letras = contar_tipo_caracteres(cadena,"letra")
    cantidad_numeros = contar_tipo_caracteres(cadena,"numero")
    cantidad_simbolos = contar_tipo_caracteres(cadena,"simbolo")
    cantidad_espacios = contar_tipo_caracteres(cadena,"espacio")

    print(f"Cantidad de letras: {cantidad_letras}")
    print(f"Cantidad de números: {cantidad_numeros}")
    print(f"Cantidad de símbolos: {cantidad_simbolos}")
    print(f"Cantidad de espacios: {cantidad_espacios}")


