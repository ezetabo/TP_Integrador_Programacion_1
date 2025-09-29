from b_funciones_csv import *
from e_funciones_generales import *

paises = []
filtrados = []
continentes = ["Africa", "America del norte", "America del sur","America central", "Europa", "Asia", "Oceania", "Todos"]
menu_principal = ["Cargar archivo .csv", "Buscar país", "Filtrar países", "Ordenar países", "Mostrar estadísticas", "Salir"]
menu_filtrado = ["Fitrar por contiente", "Filtrar rango de poblacion", "Filtrar por rango de superficie" ]
menu_ordenamiento = ["nombre", "poblacion", "superficie"]
menu_estadisticas = ["País con mayor y menor población", "País con mayor y menor superficie", "Promedio de población", "Promedio de superficie","Cantidad de países por continente"]

while True:        
    dibujar_titulo("menu principal",tab=1,char="=",cant=7)    
    match pedir_opcion_listado("Seleccione una opción: ",menu_principal):
        case 1:
            try:
                cargar_paises(paises)
            except FileNotFoundError:
                resultado ="Error: No se seleccionó o no se encontró el archivo CSV."
            except TypeError as te:
                resultado =f"Error de tipo: {te}"
            except ValueError as ve:
                resultado =f"Archivo cargado con errores: {ve}"               
            except Exception as ex:
                resultado =f"Error inesperado: {ex}"
            else:
                resultado ="Carga completada con éxito."
            dibujar_titulo(f"{resultado}",char="*",cant=3)
        case 2:
            dibujar_titulo("Buscar pais (coincidencia parcial o exacta)",char="-", cant=3)
            if not paises:
                dibujar_titulo(f"Debe cargar un archivo para poder operar",char="*",cant=3)
                continue
            mostrar_paises(buscar_paises_por_nombre(paises,pedir_cadena_solo_letras("Ingrese el nombre del pais que quiere ver: ")))
        case 3:
            dibujar_titulo("Filtrar paises",char="-", cant=3)
            if not paises:
                dibujar_titulo(f"Debe cargar un archivo para poder operar",char="*",cant=3)
                continue
            opcion = pedir_opcion_listado("Selecciones una opcion: ",menu_filtrado)
            if opcion == 1:               
                filtrados = filtrar_por_continente(paises,continente=continentes[pedir_opcion_listado("Seleccione el continente: ", continentes)-1])
            else:
                rango_minimo = pedir_entero("Ingrese la cantidad minima: ",minimo=1)
                rango_maximo = pedir_entero("Ingrese la cantidad maxima: ",minimo=2)                
                filtrados = filtrar_por_rango(paises, campo="poblacion" if opcion == 2 else "superficie",minimo=rango_minimo, maximo=rango_maximo)                
            if filtrados:
                mostrar_paises(filtrados)
            else:
                dibujar_titulo("No se econtraron registros con los critrerios de busqueda",char="*",cant=3)
        case 4:
            dibujar_titulo("Ordenar paises",char="-", cant=3)
            if not paises:
                dibujar_titulo(f"Debe cargar un archivo para poder operar",char="*",cant=3)
                continue
            print("Ordenar por:",end=" ")
            opcion = pedir_opcion_listado("Seleccione una opcion: ", menu_ordenamiento)
            asc = True if pedir_entero("Seleccione (1-Ascendente 2-Descedendete): ",minimo=1,maximo=2) == 2 else False
            mostrar_paises(ordenar_paises(paises,clave=menu_ordenamiento[opcion-1],descendente=asc))
        case 5:
            dibujar_titulo("Mostrar estadisticas",char="-", cant=3)
            if not paises:
                dibujar_titulo(f"Debe cargar un archivo para poder operar",char="*",cant=3)
                continue
            match pedir_opcion_listado("Elija que estadistica quiere ver: ",menu_estadisticas):
                case 1:
                    dibujar_titulo("Pais con menor poblacion",char="-",cant=1)  
                    mostrar_pais_con_un_campo(pais=buscar_menor_campo(paises,campo="poblacion"),campo="poblacion")
                    dibujar_titulo("Pais con mayor poblacion",char="-",cant=1)  
                    mostrar_pais_con_un_campo(pais=buscar_mayor_campo(paises,campo="poblacion"),campo="poblacion")
                case 2:
                    dibujar_titulo("Pais con menor superficie",char="-",cant=1)
                    mostrar_pais_con_un_campo(pais=buscar_menor_campo(paises,campo="superficie"),campo="superficie")
                    dibujar_titulo("Pais con mayor superficie",char="-",cant=1)
                    mostrar_pais_con_un_campo(pais=buscar_mayor_campo(paises,campo="superficie"),campo="superficie")
                case 3:
                    dibujar_titulo("Promedio de población",char="-",cant=1)
                    mostrar_promedios_por_continente(paises=paises,continentes=continentes,campo="poblacion")
                case 4:
                    dibujar_titulo("Promedio de superficie",char="-",cant=1)
                    mostrar_promedios_por_continente(paises=paises,continentes=continentes,campo="superficie")
                case 5:
                    dibujar_titulo("Cantidad de países por continente",char="-",cant=1)
                    mostrar_cantidad_paises_por_continente(paises=paises,continentes=continentes)            
        case 6:
            dibujar_titulo("Fin del programa",char="-", cant=3)
            break