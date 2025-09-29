import csv
import tkinter as tk
from tkinter import filedialog
from d_modelo import crear_pais

ENCABEZADOS_ESPERADOS = ["nombre", "poblacion", "superficie", "continente"]
def cargar_paises(lista_paises):
    """
    Carga paises desde un archivo CSV seleccionado por el usuario.
    
    La funcion abre un dialogo grafico para que el usuario seleccione un
    archivo CSV. Luego valida que el archivo tenga los encabezados correctos
    y procesa cada fila. Los registros validos se agregan a "lista_paises",
    mientras que los invalidos se contabilizan y se reportan al final.
    
    Parametros:
        lista_paises (list): Lista donde se almacenaran los paises cargados.
        
    Lanza:
        FileNotFoundError: Si el usuario cancela la seleccion.
        TypeError: Si el archivo seleccionado no es un CSV.
        ValueError: Si el CSV contiene filas con errores de conversion.
        Exception: Otros errores inesperados.       
    """
        
    # Crear ventana oculta para abrir dialogo de archivo
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.attributes("-topmost", True) # filedialog toma el foco principal
    # Abrir dialogo grafico para seleccionar archivo
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")]
    )
    root.destroy()
    
    # Si el usuario cancela el dialogo, lanzar excepcion
    if not ruta:
        raise FileNotFoundError("No se selecciono ningún archivo.")
    
    # Verificar que el archivo seleccionado sea CSV
    if not ruta.lower().endswith(".csv"):
        raise TypeError(f"El archivo seleccionado no es CSV: {ruta}")
    
    errores_conversion = []
    # Abrir archivo CSV seleccionado
    with open(ruta, newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)        
        
        # Verificar que los encabezados sean los esperados.
        if lector.fieldnames != ENCABEZADOS_ESPERADOS:
            raise ValueError(f"Encabezados incorrectos. Se esperaban {ENCABEZADOS_ESPERADOS} pero se encontraron {lector.fieldnames}")
        
        for numero_fila,fila in enumerate(lector, start=2):            
            try:
                pais = crear_pais(
                    fila["nombre"].strip(),
                    int(fila["poblacion"]),
                    float(fila["superficie"]),
                    fila["continente"].strip()
                )
                lista_paises.append(pais)
            except Exception:                
                errores_conversion.append(numero_fila)
                
    # Si hubo errores se lanza la excepcion con el resumen
    if errores_conversion:
        raise ValueError(f"Se encontraron {len(errores_conversion)} errores de conversion en las filas: {errores_conversion}")