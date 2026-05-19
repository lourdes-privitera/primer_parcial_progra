from validaciones import (
    validar_entero,
    ingresar_contrasena,
    validar_nivel_seguridad
)

from menu import mostrar_menu

from utilidades import (
    mostrar_cantidad_caracteres,
    calcular_porcentaje
)

from analisis import (
    pedir_caracter,
    buscar_caracter,
    invertir_cadena,
    verificar_palindromo,
    ordenar_contrasena,
    reporte_estadistico
)

bandera_contraseña = False #cuando ingresen el 1 , se transforma ls bandera y puedo acceder a las opciones del menu 2 a 8  
bandera_programa = True

while bandera_programa: #DIJO NO USAR WHILE TRUE (USAR BANDERA¿?)
    mostrar_menu()
    opcion = input("Seleccionar opcion: ")
    
    while not validar_entero(opcion, 1, 9):
        opcion = input("Reingrese una opcion valida:  ")

    opcion = int(opcion)
        
    if opcion == 1:
        contrasena = ingresar_contrasena()
        print("---Contraseña ingresada con exito!---")
        bandera_contraseña = True
    elif opcion == 2 and bandera_contraseña == True: 
        nivel_seguridad = validar_nivel_seguridad(contrasena)
        print(f"Nivel de seguridad: {nivel_seguridad}")

    elif opcion == 3 and bandera_contraseña == True:
        mostrar_cantidad_caracteres(contrasena)

    elif opcion == 4 and bandera_contraseña == True:
        caracter = pedir_caracter()
        buscar_caracter(contrasena, caracter)

    elif opcion == 5 and bandera_contraseña == True:
        contrasena_invertida = invertir_cadena(contrasena)
        print(f"Contraseña original: {contrasena}")
        print(f"Contraseña invertida: {contrasena_invertida}")

    elif opcion == 6 and bandera_contraseña == True:
        reporte_estadistico(contrasena) 

    elif opcion == 7 and bandera_contraseña == True: 
        verificacion = verificar_palindromo(contrasena)
        if verificacion == True:
            print("La contraseña es palíndromo")
        else:
            print("La contraseña NO es palíndromo")

    elif opcion == 8 and bandera_contraseña == True:
        orden = input("Ingrese tipo de orden (ascendente/descendente): ") #no llego a hacer una funcion que pida y valide el orden , la hago así para almenos presentar algo
        while orden != "ascendente" and orden != "descendente":
            orden = input("Reingrese ascendente o descendente: ")
        contrasena_ordenada = ordenar_contrasena(contrasena, orden)
        print(f"Contraseña original: {contrasena}")
        print(f"Contraseña ordenada: {contrasena_ordenada}")
        
    elif opcion == 9:
        print("SALIENDO...")
        bandera_programa = False
    else:
        print(f"¡¡¡NO SE PUEDE ACCEDER A LA OPCION {opcion} SIN CARGAR LA CONTRASEÑA!!! ")
    input("Toque cualquier boton para continuar...")