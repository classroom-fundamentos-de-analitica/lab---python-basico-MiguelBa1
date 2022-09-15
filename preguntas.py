"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = open("data.csv", "r")
    cont = 0
    for elem in data:
        cont += int(elem[2])
    return cont

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos = list(open("data.csv", "r"))
    letras = list(set([elem[0] for elem in datos]))
    fin = []
    for elem in letras:
        cont = 0
        for linea in datos:
            if linea[0] == elem:
                cont += 1
        fin.append((elem, cont))
    fin = sorted(fin)
    return fin

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos = list(open("data.csv", "r"))
    lista = []
    for elemento in datos:
        if elemento[0] not in lista:
            lista.append(elemento[0])
    tupla = ()
    lista2 = []

    for elmt in lista:
        suma = 0
        for cols in datos:
            if elmt == cols[0]:
                suma += int(cols[2])
        tupla = (elmt, suma)
        lista2.append(tupla)
    
    lista2 = sorted(lista2)
    return lista2

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    datos = open("data.csv", "r")
    datos = [elem.replace("\n", "").split("\t") for elem in datos]
    meses = list(set([(elem[2].split("-"))[1] for elem in datos]))
    fin = []
    for elem in meses:
        cont = 0
        for linea in datos:
            mes = linea[2].split('-')[1]
            if mes == elem:
                cont += 1
        fin.append((elem, cont))
    fin = sorted(fin)
    return fin

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos = list(open("data.csv", "r"))
    lista = []
    for elemento in datos:
        if elemento[0] not in lista:
            lista.append(elemento[0])
    tupla = ()
    lista2 = []
    

    for elmt in lista:
        nums = []
        for cols in datos:
            if elmt == cols[0]:
                nums.append(int(cols[2]))   
        tupla = (elmt, max(nums), min(nums))
        lista2.append(tupla)
    
    lista2 = sorted(lista2, key=lambda x: ord(x[0]))
    
    return lista2


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    datos = open("data.csv", "r")
    datos = [elem.replace("\n", "").split("\t") for elem in datos] 
    matrizPares = [elem[4].split(',') for elem in datos]
    pares = []
    for elem in matrizPares:
        for elem2 in elem:
            pares.append(elem2)
    letras = {}
    for elem in pares:
        elem = elem.split(":")
        if elem[0] in letras:
            letras[elem[0]].append(int(elem[1]))
        else:
            letras[elem[0]] = [int(elem[1])]
    fin = []
    for elem in letras:
        tupla = (elem, min(letras[elem]), max(letras[elem]))
        fin.append(tupla)
    fin = sorted(fin)
    return fin


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos = list(open("data.csv", "r"))
    lista = []
    for elemento in datos:
        if int(elemento[2]) not in lista:
            lista.append(int(elemento[2]))
    tupla = ()
    salida = []
    for elmt in lista:
        lista2 = []
        for cols in datos:
            if elmt == int(cols[2]):
                lista2.append(str(cols[0]))
        tupla = (elmt, lista2)
        salida.append(tupla)
    salida = sorted(salida, key=lambda x: x[0])
    return salida

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    datos = open("data.csv", "r")
    datos = [elem.replace("\n", "").split("\t") for elem in datos] 
    nums = {}
    for linea in datos:
        num = int(linea[1])
        if num in nums:
            nums[num].append(linea[0])
        else:
            nums[num] = [linea[0]]
    fin = []
    for elem in nums:
        fin.append((elem, sorted(list(set(nums[elem])))))
    fin = sorted(fin)
    return fin


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    datos = open("data.csv", "r")
    datos = [elem.replace("\n", "").split("\t") for elem in datos] 
    matrizPares = [elem[4].split(',') for elem in datos]
    pares = []
    for elem in matrizPares:
        for elem2 in elem:
            pares.append(elem2)
    letras = list(set([elem.split(':')[0] for elem in pares]))
    fin = {}
    for letra in letras:
        for par in pares:
            if letra in fin:
                if par.split(":")[0] == letra:
                    fin[letra] += 1
            elif par.split(":")[0] == letra:
                fin[letra] = 0
    return fin

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    datos = open("data.csv", "r")
    datos = [elem.replace("\n", "").split("\t") for elem in datos] 
    lista = []
    tupla = ()
    for col in datos:
        x = col[4].split(",")
        y = col[3].split(",")
        tupla = (col[0], len(y), len(x))
        lista.append(tupla)
    
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    datos = open("data.csv", "r")
    datos = [elem.replace("\n", "").split("\t") for elem in datos] 
    fin = {}
    for linea in datos:
        num = int(linea[1])
        letras = linea[3].split(",")
        for letra in letras:
            if letra in fin:
                fin[letra] += num
            else:
                fin[letra] = num
    fin = sorted(fin.items())
    fin = dict(fin)
    return fin

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    datos = open("data.csv", "r")
    datos = [elem.replace("\n", "").split("\t") for elem in datos]
    fin = {}
    for linea in datos:
        letra = linea[0]
        pares = linea[4].split(",")
        nums = []
        for par in pares:
            nums.append(int(par.split(":")[1]))
        if letra in fin:
            fin[letra] += sum(nums)
        else:
            fin[letra] = sum(nums)
    fin = sorted(fin.items())
    fin = dict(fin)
    return fin