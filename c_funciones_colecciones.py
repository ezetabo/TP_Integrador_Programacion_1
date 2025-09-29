from sys import maxsize

# =====================
# Mostrar informacion
# =====================
def mostrar_lista(lista):
    """
    Muestra los elementos de una lista en forma enumerada
    Parámetros:
        lista (list): Lista de elementos a mostrar.
    Retorno:
        None
    """ 
    print()
    for i, elemento in enumerate(lista):
        print(f"{i+1:>3}. {elemento:<50}")

def mostrar_paises(paises):
    """
    Muestra en formato tabular una lista de países con sus principales datos.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        
    Retorno:
        None
    """
    print(f"•{"-"*107}•")
    print(f"| {"Nombre":>20} {"|":>21} {"Datos":>23} {"|":>17} {"Continente":>15}{"|":>7}")    
    print(f"•{"-"*107}•")    
    for indice,pais in enumerate(paises):
        print(f"| {indice+1:>3}. {pais["nombre"]:<35} | Pob: {pais["poblacion"]:>13,} | Sup: {pais["superficie"]:>13,.12g} | {pais["continente"]:<20} {"|"}")
    print(f"•{"-"*107}•")   

def mostrar_cantidad_paises_por_continente(*,paises, continentes):
    """
    Muestra la cantidad de países agrupados por continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        
    Retorno:
        None
    """
    print(f"•{"-"*42}•")
    print(f"| {"Continente":>10} {"|":>15} {"Cant. paises":>5} {"|":>2}")    
    print(f"•{"-"*42}•") 
    for indice,continente in enumerate(continentes,start=1):
        print(f"| {indice:>2}. {continente:<18} {"|":>3} {contar_paises_por_continente(paises=paises,continente=continente):>5}{"|":>10}")
    print(f"•{"-"*42}•")

def mostrar_promedios_por_continente(*,paises, continentes,campo):
    """
    Muestra el promedio de un campo numérico (ejemplo: población, superficie) agrupado por continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continentes (list[str]): Lista de continentes a evaluar.
        campo (str): Nombre del campo numérico sobre el cual calcular el promedio.
        
    Retorno:
        None
    """
    print(f"•{"-"*52}•")
    print(f"| {"Continente":>10} {"|":>15} {f"Promedio {campo}":<20} {"|":>4}")    
    print(f"•{"-"*52}•") 
    for indice,continente in enumerate(continentes,start=1):
        print(f"| {indice:>2}. {continente:<18} {"|":>3} {calcular_promedio_por_continente(paises,continente=continente,campo=campo):>15,.0f}{"|":>10}")
    print(f"•{"-"*52}•")

def mostrar_pais_con_un_campo(*,pais,campo):
    """
    Muestra un país y el valor de un campo específico.
    
    Parámetros:
        pais (dict): Diccionario con los datos del país.
        campo (str): Nombre del campo a mostrar.
        
    Retorno:
        None
    """
    print(f"•{"-"*50}•")
    print(f"| {"Nombre":>10} {"|":>15} {f"{campo}":>14} {"|":>8}")    
    print(f"•{"-"*50}•")     
    print(f"| {" ":>2}. {pais["nombre"]:<18} {"|":>3} {pais[campo]:>15,.12g}{"|":>8}")
    print(f"•{"-"*50}•")

# =====================
# Busquedas
# =====================
def buscar_paises_por_nombre(paises, nombre):
    """
    Busca países por coincidencia exacta o parcial en una lista de diccionarios.
        
    Parámetros
    paises : list[dict]
        Lista de países representados como diccionarios.
    nombre : str
        Nombre (o parte del nombre) del país a buscar.
        La comparación no distingue entre mayúsculas y minúsculas.
        
    Retorna
        
    list[dict]
        - Si encuentra una coincidencia exacta, devuelve una lista con un solo diccionario correspondiente a ese país.
        - Si no hay coincidencia exacta, devuelve una lista con todos los países cuyo nombre contenga la cadena buscada.
        - Si no encuentra ninguna coincidencia, devuelve una lista vacía.
    """    
    encontrados = []    
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            encontrados.append(pais)
            break
        elif pais["nombre"].lower().startswith(nombre.lower()):
            encontrados.append(pais)    
    return encontrados

def buscar_mayor_campo(paises,*,campo="poblacion"):
    """
    Busca el país que posee el mayor valor en un campo numérico.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        campo (str): Campo numérico a evaluar (por defecto "poblacion").
        
    Retorno:        
        El país con el mayor valor en el campo especificado.
    """
    mayor_valor = -maxsize-1
    mayor_pais = {}
    for pais in paises:
        if pais[campo.lower()] > mayor_valor:
            mayor_valor = pais[campo.lower()]
            mayor_pais = pais
    return mayor_pais

def buscar_menor_campo(paises,*,campo="poblacion"):
    """
    Busca el país que posee el menor valor en un campo numérico.
        
    Parámetros:
        paises (list[dict]): Lista de países.
        campo (str): Campo numérico a evaluar (por defecto "poblacion").
        
    Retorno:
        El país con el menor valor en el campo especificado.
    """
    menor_valor = maxsize
    menor_pais = {}
    for pais in paises:
        if pais[campo.lower()] < menor_valor:
            menor_valor = pais[campo.lower()]
            menor_pais = pais
    return menor_pais

# =====================
# Filtros
# =====================
def filtrar_por_continente(paises, *, continente="todos"):
    """
    Filtra los países según el continente especificado.

    Parámetros:
        paises (list[dict]): Lista de países.
        continente (str): Nombre del continente por el cual filtrar("todos" para no aplicar filtro).
        
    Retorno:
        list[dict]: 
            Lista de países pertenecientes al continente solicitado.
    """
    filtrados = []
    for pais in paises:
        if (pais["continente"].lower() == continente.lower()) or continente.lower() == "todos":
            filtrados.append(pais)
    return filtrados

def filtrar_por_rango(paises,*,campo ,minimo, maximo):
    """
    Filtra los países cuyos valores en un campo numérico estén dentro de un rango.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        campo (str): Nombre del campo numérico a evaluar.
        minimo (int | float): Valor mínimo aceptado.
        maximo (int | float): Valor máximo aceptado.
        
    Retorno:
        list[dict]
            Lista de países que cumplen con la condición de rango.
    """
    filtrados = []
    for pais in paises:
        if minimo <= pais[campo] and pais[campo] <= maximo:
            filtrados.append(pais)
    return filtrados  

# =====================
# Ordenamientos
# =====================
def ordenar_paises(paises,*, clave="nombre", descendente=False):
    """
    Ordena una lista de países en función de un campo dado.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        clave (str): Campo por el cual ordenar (por defecto "nombre").
        descendente (bool): Si es False (por defecto), ordena ascendente.
                            Si es True, ordena de forma descendente. 
                            
    Retorno:
        list[dict]
            Lista de países ordenada según los criterios indicados.
    """
    return sorted(paises, key=lambda pais: pais[clave], reverse=descendente)


# =====================
# Estadísticas
# =====================

def contar_paises_por_continente(paises,*,continente="todos"):
    """
    Cuenta la cantidad de países pertenecientes a un continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continente (str): Nombre del continente a evaluar("todos" para contar global).
    Retorno:
        int
            Cantidad de países en el continente especificado.
    """
    contador = 0
    for pais in paises:
        if (pais["continente"].lower() == continente.lower()) or continente.lower() == "todos":
            contador += 1
    return contador

def calcular_promedio_por_continente(paises,*,continente="amrica del sur",campo="poblacion"):
    """
    Calcula el promedio de un campo numérico para un continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continente (str): Nombre del continente a evaluar("todos" para global).                       
        campo (str): Campo numérico sobre el cual calcular el promedio(por defecto "poblacion").
    Retorno:
        float
            Promedio del campo solicitado para el continente especificado.
    """
    acumulador = 0
    cantidad_paises = contar_paises_por_continente(paises,continente=continente)
    for pais in paises:
        if (pais["continente"].lower() == continente.lower()) or continente.lower() == "todos":
            acumulador += pais[campo.lower()]
    promedio = acumulador / cantidad_paises
    return promedio


