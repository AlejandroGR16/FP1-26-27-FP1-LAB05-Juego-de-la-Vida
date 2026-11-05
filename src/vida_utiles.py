import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    return [[False for c in range(columnas)] for f in range(filas)]

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    return [[(random.random()<probabilidad_vida) for c in range(columnas)] for f in range(filas)]

def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """
    for f in range(len(patron)):
        for c in range(len(patron[0])):
            if f+pos_fila <= len(tablero) and c+pos_col <= len(tablero[0]):
                tablero[f+pos_fila][c+pos_col] = patron[f][c]

def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    vecinos = 0
    for i in range(-1,2):
        for j in range(-1,2):
            f=fila+i
            c=col+j
            if f >= len(tablero): f = (f % len(tablero))
            if c >= len(tablero[0]): c = (c % len(tablero[0]))
            if (not (i==0 and j==0)) and (tablero[f][c] == True):
                vecinos +=1
    return vecinos

def calcular_siguiente_generacion(tablero) -> list[list[bool]]:
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    res=crear_tablero(len(tablero),len(tablero[0]))
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            vecinos=contar_vecinos(tablero,i,j)
            if (tablero[i][j]==True) and (vecinos==2 or vecinos==3):
                res[i][j]=True
            elif (tablero[i][j]==False) and (vecinos==3):
                res[i][j]=True
            else: res[i][j]=False
    return res