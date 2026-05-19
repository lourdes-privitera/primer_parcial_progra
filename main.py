from validaciones import * #NO USAR EL ASTERISCO, LLAMAR DE A UNA ANTES DE ENTREGAR
from menu import *
from utilidades import *
from analisis import *

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
#-------------------------------------------------------FALTA PUSHEAR ESTO
    elif opcion == 2 and bandera_contraseña == True: #NO PUSHEE ESTO
        nivel_seguridad = validar_nivel_seguridad(contrasena)
        print(f"Nivel de seguridad: {nivel_seguridad}")

    elif opcion == 3 and bandera_contraseña == True:
        mostrar_cantidad_caracteres(contrasena)

    elif opcion == 4 and bandera_contraseña == True:
        caracter = pedir_caracter()
        buscar_caracter(contrasena, caracter)
#-------------------------------------------------------
    elif opcion == 9:
        print("SALIENDO...")
        bandera_programa = False
    else:
        print(f"¡¡¡NO SE PUEDE ACCEDER A LA OPCION {opcion} SIN CARGAR LA CONTRASEÑA!!! ")
    input("Toque cualquier boton para continuar...")