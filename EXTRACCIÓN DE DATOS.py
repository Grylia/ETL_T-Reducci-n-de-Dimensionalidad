import requests
import pandas as pd

# Hacer una solicitud GET a una API
url = 'https://api.ejemplo.com/datos'
response = requests.get(url)

# Suponiendo que la respuesta es un JSON que contiene una lista de diccionarios
data = response.json()

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Mostrar los datos originales
print("Datos originales:")
print(df.head())