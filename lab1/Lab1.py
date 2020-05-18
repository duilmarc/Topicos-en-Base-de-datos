from math import sqrt
import csv

def leerArchivo():
    usuarios = []
    pelicula = {}
    puntaje=[]
    with open('Movie_Ratings.csv') as File:
        reader = csv.reader(File, delimiter=',',lineterminator='\n',
                            quoting=csv.QUOTE_MINIMAL)
        
        for row in reader:
            if len(usuarios) == 0:
                for i in range(1,len(row)):
                    usuarios.append(row[i])
            else:
                for j in range(1,len(row)):
                    if(row[j]==''):
                        pelicula[row[0]]=row[j]
                    else:
                        pelicula[row[0]]=float(row[j])
                    puntaje.append(pelicula.popitem())
                    
        x=len(puntaje)/len(usuarios)
        diccionario={}
        for j in range(len(usuarios)):
            dicc_peliculas={}
            for i in range(j,len(puntaje),int(x)):
              key,value= puntaje[i]
              if(value == ''):
                  continue
              dicc_peliculas[key]=value
            diccionario[usuarios[j]] = dicc_peliculas
            
    return diccionario
						


def manhattan(rating1, rating2):
    distance = 0
    flag = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            flag = 1
    return  distance if flag  else -1

def Euclidiana(rating1, rating2):
    distance = 0
    flag = 0
    for key in rating1:
        if key in rating2:
            distance += pow( rating1[key] - rating2[key],2)
            flag = 1
    return  sqrt(distance) if flag  else -1

def Minkowski(rating1, rating2,r):
    distance = 0
    flag = 0
    for key in rating1:
        if key in rating2:
            distance += pow( abs(rating1[key] - rating2[key]),r)
            flag = 1
    return pow(distance,1/r) if flag else -1

tabla = leerArchivo()
print(manhattan(tabla["Patrick C"],tabla["Thomas"]))
print(Euclidiana(tabla["Patrick C"],tabla["Thomas"]))
print(Minkowski(tabla["Patrick C"],tabla["Thomas"],2))


