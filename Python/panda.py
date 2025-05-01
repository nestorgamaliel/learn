import pandas as pd
import numpy as np

# Ejercicio 1
serie = pd.Series([2, 4, -8, 3])
print(serie)

# Ejercicio 2
serie2 = pd.Series([2, 4, -8, 3], index=["d", "g", "t", "5"])
print(serie2)

# Ejercicio 3
print(serie2)
print(serie2["d"])
print(serie2[["g", "5"]])
print(serie2[serie2 >= 2])

# Ejercicio 4, Dataframe

data = {
    "departamento": ["San Miguel", "Chalatenango", "San Salvador", "Santa Ana", "Sonsonate"],
    "ruta": ["301", "125", "30B", "201", "205"],
    "Centro Turistico": ["Playa El Cuco", "Pital", "Centro Historico", "Catedral", "Cobanos"]}

frame = pd.DataFrame(data)

print("data")
print(data)
print("frame")
print(frame)
print("\n"*2)

# Ejercicio 5
data = {"Nombre" : ["Juan", "Marisol", "Ernesto", "Mario", "Andrea"],
        "Nota": [10, 9, 8, 5, 6],
        "Deporte": ["Futbol", "Natación", "Boxeo", "Karate", "Judo"],
        "Asignatura": ["Sistemas", "Estadistica", "Matematicas", "Fisica", 
                       "Quimica"]}

df = pd.DataFrame(data)
print(df)

print("\n"*2)


data5 = {"Nombre" : ["Juan", "Marisol", "Ernesto", "Mario", "Andrea"],
         "Nota": [10, 9, np.nan, 5, 6],
         "Deporte": ["Futbol", "Natación", "Boxeo", "Karate", "Judo"],
         "Asignatura": ["Sistemas", "Estadistica", "Matematicas", "Fisica", 
                        "Quimica"]}

df5 = pd.DataFrame(data5)
print(df5)

print(df5.info())


# Ejercicio 6
data5 = {"Nombre" : ["Juan", "Marisol", "Ernesto", "Mario", "Andrea"],
         "Nota": [10, 9, np.nan, 5, 6],
         "Deporte": ["Futbol", "Natación", "Boxeo", "Karate", "Judo"],
         "Asignatura": ["Sistemas", "Estadistica", "Matematicas", "Fisica", 
                        "Quimica"]}

df5 = pd.DataFrame(data5)
print(df5)


print("Ejercicio 6\n"*2)
print(df5.info())

print("\n"*2)
print("Describe\n")
print(df5.describe())

print("\n"*2)
print("Replace\n")
nuevo = df5.replace(np.nan, 0);
print(nuevo)


print("\n"*2)
print("Convertir a enteros\n")
nuevo["Nota"] = nuevo["Nota"].astype(int)
print(nuevo.describe())
print(nuevo.info())
print(nuevo)

print("\n"*2)
print("Estadistica\n")
print("Promedio: ", nuevo["Nota"].mean())

ruta = r"g:\My Drive\Estudios\UMA\UMA2025\Ciencia de datos\Presentaciones\4. Dataset.csv"
print(ruta)
datacsv = pd.read_csv(ruta, header=0)
print(datacsv)
print(datacsv.head())
print(datacsv.info())   
print(datacsv.describe())

print("\n"*2)