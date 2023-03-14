from io import open
import time


#Clase proceso
class proceso():
    nombre = ""
    tiempo = 0
    prioridad = 0

#Función para mostrar la simulación de los procesos generales
def comp(p):
    barra = ""
    print(p.nombre)
    for i in range(0,p.tiempo):
        barra = barra + "#"
        print(barra)
        time.sleep(0.35)

    return
#Función para mostrar la simulación de los procesos con RR
def comp_rr(p):
    barra = ""
    print(p.nombre)
    for i in range(0,3):
        barra = barra + "#"
        print(barra)
        p.tiempo = p.tiempo - 1
        if p.tiempo == 0:
            return True
        time.sleep(0.35)

    return

def agregar(pro_lis,tiempos,prioridades):
    res = 0
    n_p = int(input("Quiere agregar un nuevo proceso (0 N, 1 S)"))
    if(n_p):
        aux_p = proceso()
        aux_p.nombre = input("Nombre del proceso: ")
        aux_p.tiempo = int(input("Tiempo de duracion del proceso: "))
        aux_p.prioridad = int(input("Prioridad del proceso "))
        res = int(input("Quiere agregarlo al comienzo o al final(0 C, 1 F)"))
        if (res == 0):
            pro_lis.insert(0,aux_p)
            tiempos.insert(0,aux_p.tiempo)
            prioridades.insert(0,aux_p.prioridad)
            
        else:
            pro_lis.append(aux_p)
            tiempos.append(aux_p.tiempo)
            prioridades.append(aux_p.prioridad)
        return True
    return False

#Función para leer el archivo e iniciar los algoritmos de planificación
def read():
    procesos = []
    tiempos = []
    prioridades = []
    res = 1
    con = 0
    ban = True

    file = open("procesos.txt", "r")

    lines = file.readlines()

    file.close()

    #Creación de los objetos tipo proceso y registro de sus tiempos y prioridades
    for l in lines:
        aux = l.split(',')
        procesos.append(proceso())
        procesos[con].nombre = aux[0]
        procesos[con].tiempo = int(aux[1])
        procesos[con].prioridad = int(aux[2])
        tiempos.append(int(aux[1]))
        prioridades.append(int(aux[2]))
        con = con + 1

    while (ban):
        ban = agregar(procesos,tiempos,prioridades)

    #Ordenar tiempos y prioridades
    tiempos.sort()
    prioridades.sort()

    
    while (0 < res < 5):
        res = int(input("Que algoritmo quieres utilizar\n       1.FIFO\n       2.SJF\n       3.Prioridades\n        4.RoundRobin\n"))
        if(res == 1):
            fifo(procesos)
        elif(res == 2):
            sjf(procesos,tiempos)
        elif(res == 3):
            prio(procesos,prioridades)
        elif(res == 4):
            rr(procesos)
        else:
            print("Opcion no valida")

    return 

    #Planeación FIFO (Por orden de llegada)
def fifo(procesos):
    print("-----------FIFO-----------")
    for p in procesos:
        comp(p)

    return

    #Planeación SJF (Por tiempo)
def sjf(procesos,tiempos):
    print("-----------SJF-----------")
    aux_o = procesos.copy()
    for i in tiempos:
        for p in aux_o:
            if p.tiempo == i:
                comp(p)
                aux_o.remove(p)

    return
    
    #Planeación por prioridad
def prio(procesos,prioridades):
    print("-----------Prioridad-----------")
    aux_p = procesos.copy()
    for j in prioridades:
        for pr in aux_p:
            if pr.prioridad == j:
                comp(pr)
                aux_p.remove(pr)
    
    return

    #Planeación por RR
def rr(procesos):
    print("-----------Round Robin-----------")
    b=True
    aux_l = procesos.copy()

    l=len(aux_l)-1

    while(aux_l):
        cont = 0
        while(cont<l):
            if comp_rr(aux_l[cont]):
                aux_l.remove(aux_l[cont])
                l=len(aux_l)-1
                cont = cont - 1
            cont = cont + 1
        if comp_rr(aux_l[cont]):
                aux_l.remove(aux_l[cont])
                l=len(aux_l)-1
        
    return





read()