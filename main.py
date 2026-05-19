from validaciones import * #NO USAR EL ASTERISCO, LLAMAR DE A UNA ANTES DE ENTREGAR
from menu import *

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

    elif opcion == 9:
        print("SALIENDO...")
        bandera_programa = False
    else:
        print(f"¡¡¡NO SE PUEDE ACCEDER A LA OPCION {opcion} SIN CARGAR LA CONTRASEÑA!!! ")
    input("Toque cualquier boton para continuar...")