import copy

def primer_ajuste(bloques, procesos):
    asignacion = [-1] * len(procesos)
    for i, proceso in enumerate(procesos):
        for j, bloque in enumerate(bloques):
            if bloque >= proceso:
                asignacion[i] = j
                bloques[j] -= proceso
                break
    return asignacion

def mejor_ajuste(bloques, procesos):
    asignacion = [-1] * len(procesos)
    for i, proceso in enumerate(procesos):
        mejor_idx = -1
        for j, bloque in enumerate(bloques):
            if bloque >= proceso:
                if mejor_idx == -1 or bloques[j] < bloques[mejor_idx]:
                    mejor_idx = j
        if mejor_idx != -1:
            asignacion[i] = mejor_idx
            bloques[mejor_idx] -= proceso
    return asignacion

def peor_ajuste(bloques, procesos):
    asignacion = [-1] * len(procesos)
    for i, proceso in enumerate(procesos):
        peor_idx = -1
        for j, bloque in enumerate(bloques):
            if bloque >= proceso:
                if peor_idx == -1 or bloques[j] > bloques[peor_idx]:
                    peor_idx = j
        if peor_idx != -1:
            asignacion[i] = peor_idx
            bloques[peor_idx] -= proceso
    return asignacion

def siguiente_ajuste(bloques, procesos):
    asignacion = [-1] * len(procesos)
    ultimo_asignado = 0
    for i, proceso in enumerate(procesos):
        for j in range(len(bloques)):
            idx = (ultimo_asignado + j) % len(bloques)
            if bloques[idx] >= proceso:
                asignacion[i] = idx
                bloques[idx] -= proceso
                ultimo_asignado = idx
                break
    return asignacion

def ingresar_datos():
    bloques = []
    procesos = []
    print("Ingrese los tamaños de los bloques de memoria (F para finalizar):")
    while True:
        val = input(f"Tamaño del bloque {len(bloques) + 1}: ")
        if val.upper() == 'F':
            break
        bloques.append(int(val))
    print("Ingrese los tamaños de los procesos (F para finalizar):")
    while True:
        val = input(f"Tamaño del proceso {len(procesos) + 1}: ")
        if val.upper() == 'F':
            break
        procesos.append(int(val))
    return bloques, procesos

def mostrar_resultados(nombre, asignacion, bloques):
    print(f"\n{nombre}:")
    for i, asignado in enumerate(asignacion):
        print(f"Proceso {i + 1} ({procesos[i]} KB) -> ", end="")
        if asignado != -1:
            print(f"Bloque {asignado + 1}")
        else:
            print("No asignado")
    print(f"Bloques disponibles: {bloques}")

def comparar_algoritmos(bloques, procesos):
    resultados = []
    for nombre, funcion in [("Primer Ajuste", primer_ajuste), ("Mejor Ajuste", mejor_ajuste), ("Peor Ajuste", peor_ajuste), ("Siguiente Ajuste", siguiente_ajuste)]:
        copia_bloques = copy.deepcopy(bloques)
        asignacion = funcion(copia_bloques, procesos)
        procesos_asignados = sum(1 for a in asignacion if a != -1)
        memoria_desperdiciada = sum(copia_bloques)
        resultados.append((nombre, procesos_asignados, memoria_desperdiciada))
    print("\nComparación de algoritmos:")
    print(f"{'Algoritmo':<20}{'Procesos Asignados':<20}{'Memoria Desperdiciada'}")
    for nombre, asignados, desperdicio in resultados:
        print(f"{nombre:<20}{asignados:<20}{desperdicio}")

if __name__ == "__main__":
    print("Bienvenido al simulador de asignación de memoria")
    bloques, procesos = ingresar_datos()
    
    for algoritmo, funcion in [("Primer Ajuste", primer_ajuste), ("Mejor Ajuste", mejor_ajuste), ("Peor Ajuste", peor_ajuste), ("Siguiente Ajuste", siguiente_ajuste)]:
        copia_bloques = copy.deepcopy(bloques)
        asignacion = funcion(copia_bloques, procesos)
        mostrar_resultados(algoritmo, asignacion, copia_bloques)
    
    comparar_algoritmos(bloques, procesos)
